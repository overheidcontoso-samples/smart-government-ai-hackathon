import os
import xml.etree.ElementTree as ET
import shutil

NAMESPACES = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'pic': 'http://schemas.openxmlformats.org/drawingml/2006/picture',
    'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing',
}

EMU_PER_PIXEL = 9525  # Approximately, at 96 DPI

def get_rels(rels_path):
    rels = {}
    if not os.path.exists(rels_path):
        return rels
    try:
        tree = ET.parse(rels_path)
        root = tree.getroot()
        ns = '{http://schemas.openxmlformats.org/package/2006/relationships}'
        for child in root.findall(f'{ns}Relationship'):
            rid = child.get('Id')
            target = child.get('Target')
            rels[rid] = target
    except Exception as e:
        print(f"Error parsing rels {rels_path}: {e}")
    return rels

def add_icons(text):
    text_lower = text.lower()
    if "lab" in text_lower and ("1" in text or "2" in text or "3" in text):
        return "🧪 " + text
    if "tip" in text_lower:
        return "💡 " + text
    if "belangrijk" in text_lower or "warning" in text_lower or "let op" in text_lower:
        return "⚠️ " + text
    if "stap" in text_lower:
        return "👣 " + text
    if "inloggen" in text_lower or "sign in" in text_lower:
        return "🔑 " + text
    if "download" in text_lower:
        return "⬇️ " + text
    if "fabric" in text_lower:
        return "🏭 " + text # Factory for Fabric :)
    if "agent" in text_lower:
        return "🤖 " + text
    return text

def parse_document(doc_path, rels_path, media_src_dir, media_dest_dir, output_file):
    print(f"Parsing {doc_path}...")
    rels = get_rels(rels_path)
    
    try:
        tree = ET.parse(doc_path)
        root = tree.getroot()
    except Exception as e:
        print(f"Error parsing {doc_path}: {e}")
        return

    body = root.find('w:body', NAMESPACES)
    if body is None:
        print(f"No body found in {doc_path}")
        return
    
    if not os.path.exists(media_dest_dir):
        os.makedirs(media_dest_dir)

    md_lines = []
    
    # Track list state
    in_list = False
    
    for p in body.findall('w:p', NAMESPACES):
        p_text = ""
        pPr = p.find('w:pPr', NAMESPACES)
        
        # 1. Heading Detection
        style_val = None
        if pPr is not None:
             pStyle = pPr.find('w:pStyle', NAMESPACES)
             if pStyle is not None:
                 style_val = pStyle.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val')
        
        heading_level = 0
        if style_val and style_val.startswith('Heading'):
             try:
                 heading_level = int(style_val.replace('Heading', ''))
             except:
                 pass
        
        # 2. List Detection
        is_list = False
        ilvl = 0
        if pPr is not None:
            numPr = pPr.find('w:numPr', NAMESPACES)
            if numPr is not None:
                is_list = True
                ilvl_elem = numPr.find('w:ilvl', NAMESPACES)
                if ilvl_elem is not None:
                    ilvl = int(ilvl_elem.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val'))

        # Process Runs
        p_images = []
        p_runs_text = []
        
        for child in p:
            tag = child.tag
            tag_name = tag.split('}')[-1] if '}' in tag else tag
            
            if tag_name == 'r': # Run
                rPr = child.find('w:rPr', NAMESPACES)
                run_text = ""
                is_run_code = False
                
                # Check for code font
                if rPr is not None:
                    rFonts = rPr.find('w:rFonts', NAMESPACES)
                    if rFonts is not None:
                        ascii_font = rFonts.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}ascii')
                        hAnsi_font = rFonts.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}hAnsi')
                        if (ascii_font and ('Consolas' in ascii_font or 'Courier' in ascii_font)) or \
                           (hAnsi_font and ('Consolas' in hAnsi_font or 'Courier' in hAnsi_font)):
                            is_run_code = True
                
                # Text
                for t in child.findall('w:t', NAMESPACES):
                    if t.text:
                        text_val = t.text
                        if is_run_code:
                            text_val = f"`{text_val}`"
                        run_text += text_val
                
                p_runs_text.append(run_text)

                # Images
                for drawing in child.findall('.//w:drawing', NAMESPACES):
                    # Get dimensions
                    width_px = None
                    try:
                        extent = drawing.find('.//wp:extent', NAMESPACES)
                        if extent is not None:
                            cx = int(extent.get('cx', 0))
                            width_px = round(cx / EMU_PER_PIXEL)
                    except:
                        pass
                    
                    blips = drawing.findall('.//a:blip', NAMESPACES)
                    for blip in blips:
                        embed_id = blip.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
                        if embed_id and embed_id in rels:
                            target = rels[embed_id]
                            filename = os.path.basename(target)
                            src_path = os.path.join(media_src_dir, filename)
                            dest_path = os.path.join(media_dest_dir, filename)
                            
                            if os.path.exists(src_path):
                                shutil.copy(src_path, dest_path)
                                p_images.append({'filename': filename, 'width': width_px})

            elif tag_name == 'hyperlink':
                 rid = child.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
                 link_target = rels.get(rid, "")
                 link_text = ""
                 for r in child.findall('w:r', NAMESPACES):
                     for t in r.findall('w:t', NAMESPACES):
                         if t.text:
                             link_text += t.text
                 if link_text:
                     p_runs_text.append(f"[{link_text}]({link_target})")

        full_text = "".join(p_runs_text).strip()

        # Output Logic
        
        # Lists
        if is_list:
            if not in_list:
                md_lines.append("") 
            in_list = True
            indent = "  " * ilvl
            md_lines.append(f"{indent}- {full_text}")
        
        # Not a list
        else:
            if in_list:
                md_lines.append("") 
                in_list = False
            
            # Headings
            if heading_level > 0:
                full_text = add_icons(full_text)
                md_lines.append(f"\n{'#' * heading_level} {full_text}\n")
            
            elif full_text:
                # Naive Keyword Detection for "Steps" or "Labs" if not marked as heading in Word
                lower_text = full_text.lower()
                if (lower_text.startswith("stap") and len(full_text) < 80) or \
                   (lower_text.startswith("lab") and len(full_text) < 80) or \
                   (lower_text.startswith("deel") and len(full_text) < 80) or \
                   (full_text.endswith(":") and len(full_text) < 80):
                        
                        full_text = add_icons(full_text)
                        md_lines.append(f"\n### {full_text}\n")
                else:
                    md_lines.append(full_text)
                    md_lines.append("")

        # Append Images
        for img in p_images:
            filename = img['filename']
            width = img['width']
            if width and width < 600:
                 md_lines.append(f'\n<img src="images/{filename}" width="{width}px" alt="{filename}">\n')
            else:
                 md_lines.append(f'\n<img src="images/{filename}" alt="{filename}">\n')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_lines))
    print(f"Created {output_file}")

def main():
    base_path = os.getcwd() 
    
    # Data_Agent_Labs
    print("Processing Data_Agent_Labs...")
    parse_document(
        os.path.join(base_path, "temp/Data_Agent_Labs/word/document.xml"),
        os.path.join(base_path, "temp/Data_Agent_Labs/word/_rels/document.xml.rels"),
        os.path.join(base_path, "temp/Data_Agent_Labs/word/media"),
        os.path.join(base_path, "images"),
        os.path.join(base_path, "Data_Agent_Labs.md")
    )

    # Agent_Labs
    print("Processing Agent_Labs...")
    parse_document(
        os.path.join(base_path, "temp/Agent_Labs/word/document.xml"),
        os.path.join(base_path, "temp/Agent_Labs/word/_rels/document.xml.rels"),
        os.path.join(base_path, "temp/Agent_Labs/word/media"),
        os.path.join(base_path, "images"),
        os.path.join(base_path, "Agent_Labs.md")
    )

if __name__ == "__main__":
    main()
