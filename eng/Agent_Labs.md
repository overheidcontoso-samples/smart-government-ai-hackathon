# Smart Government – AI Agentic Hackathon

## 🧪 Part 2 Agent lab

We are now going to work with Agents. Agents are Large Language Models (LLMs) that run in a continuous loop until a specific goal, the instructions, is reached. In that loop, they combine reasoning with access to context, such as RAG solutions, knowledge databases and can perform actions by means of tools to achieve the goal.

It is important to understand that LLMs are trained on public data and not on data within your organization. An LLM only becomes truly valuable when it is enriched with your specific context, data and processes.

Modern LLMs are also trained not only to generate answers, but also to perform actions via tools. For this we see that MCP (Model Context Protocol) is quickly developing into a standard, although there are multiple architectures and implementation options.

Agents can be deployed in different ways. We often see them in a chat-like environment, where a user asks questions in natural language and starts actions. In addition, agents can be part of workflows, where several specialized agents work together, each with their own role, such as analyzing, planning, deciding and executing.

In this way flexible, modular solutions are created in which agents handle tasks independently, direct each other and involve the user where necessary.

In this document you will walk through step by step how to log in to Azure AI Foundry, select a project and create a first agent (including linking tools such as Fabric Data Agent and Foundry IQ).

Content of the Agent Labs

- Lab 1: Log in and explore Microsoft Foundry
- Lab 2: Configure and use the Fabric Data Agent in Microsoft Foundry
- Lab 3: Creating requests agent using Foundry IQ and MCP

## 🧪 Lab 1: Log in and explore Microsoft Foundry

To get started, we will first log in to the Microsoft Foundry environment and set up a number of things to get started with Data Agents.

Before we continue

- After the introduction you received temporary login details (username and password). If not, let the instructors know.
- Download these instructions available in the GitHub repository.

Getting started with Foundry

### We will now perform the following actions:

- Log in to Microsoft Foundry with the temporary login details.
- Explore the Agent environment.

### 👣 Step 1: Log in to Microsoft Foundry

- Go to [https://ai.azure.com](https://ai.azure.com)
- Enter the username email
- Enter the received password (TAP) and press Sign in

<img src="../images/image1.png" width="253px" alt="image1.png">

- Once you are logged in you will arrive at the Foundry home page. You start on the old portal, today we are going to use the new portal. The improved functionality is available via the new portal.
- Choose in the menu for the new portal (New portal).

<img src="../images/image2.png" width="501px" alt="image2.png">

- Select the project: proj-labxx.

<img src="../images/image3.png" width="277px" alt="image3.png">

## Short explanation: Microsoft Foundry

Microsoft Foundry is the environment where you develop and manage AI solutions. The starting point is a Foundry resource: the central place where access, models and reusable agents come together.

- Projects: create one or more projects within one Foundry resource to separate use cases (or teams/environments). This keeps settings, assets and rights organized.
- Agents: within a project you create agents for different use cases (e.g. Q&A, summarizing or process/workflow automation). Agents use the models and tools available to your project.
- Models: the Foundry resource contains models that have been deployed or made available by someone with the admin role. In your project/agent you then choose the model that you are allowed and want to use.
- Tools: you can use tools that are already (partly) pre-configured, such as data sources, search/retrieval, connectors or other capabilities. This allows you to start faster without setting everything up yourself.

Briefly summarized: the Foundry resource offers the basic (access, models and shared tools). Within projects you build agents for specific use cases.

### 👣 Step 2: Explore Foundry

- Choose Build and explore the different parts of the environment.

<img src="../images/image4.png" alt="image4.png">

**End of Lab 1**

This concludes Lab 1 and we move on to Lab 2 to link a Data Agent in Microsoft Foundry

## 🧪 Lab 2: Configure and use the Fabric Data Agent in Microsoft Foundry

In this lab we will link and use a created Fabric Data Agent in a Foundry Agent.

Before we continue

- Make sure you have completed the Fabric Labs: Optionally you have access to the workspace <xxxxxx> with a data agent.

### 👣 Step 1: Create a Foundry Agent

- Go to Agents and choose Create agent.

<img src="../images/image5.png" alt="image5.png">

- Give the agent a name

<img src="../images/image6.png" width="348px" alt="image6.png">

- Fill in a first set of instructions (prompt).
  - Example instructions:
  
```
  Role: 
  You are a reliable and accurate data assistant who answers questions based on historical application data.
  Context: You work exclusively with the available historical application data.
  Goal: You help users gain insight into historical applications by answering substantive questions, recognizing patterns and summarizing trends in the data.
```

- Then choose Save and go to Add under Tools.

<img src="../images/image7.png" width="514px" alt="image7.png">

- Select Browse All Tools

<img src="../images/image40.png" width="282px" alt="image40.png">

- Select the tool Fabric Data Agent under Tools.

<img src="../images/image9.png" width="382px" alt="image9.png">

- Then fill in the Workspace ID and Artifact ID. Which you find in the following way

- Go in Fabric to the agent you created. Copy the Workspace ID and the Artifact ID from the URL.

<img src="../images/image11.png" width="529px" alt="image11.png">

<img src="../images/image10.png" width="227px" alt="image10.png">

- You can now test the agent in the chat.

<img src="../images/image12.png" width="417px" alt="image12.png">

- “Type in the chat: Give overview of applications per year ?”

- Tip: optionally add Code interpreter as a tool and ask the agent to create a graph per year, for example.

**End of Lab 2**

## 🧪 Lab 3: Creating requests agent (with Knowledge + application tool)

Two tools/data sources are already linked in the environment.

We are now going to create a requests agent using these tools.

### 👣 Step 1: Create the requests agent with knowledge

- Create a new agent

<img src="../images/image13.png" alt="image13.png">

- Use the following simple instructions (prompt):

``` 
  - Role: 
  You are a digital requests agent for a municipality. You support residents and employees in understanding, tracking and handling various types of requests.

  - Goal: 
  You answer questions about municipal requests and support the request process by:
    - Providing information based on linked knowledge bases.
    - Recognizing and starting the right request via the request tool.
    - Explaining the status and progress of existing requests.
    - If you use sources, add source references.
    - For new requests/reports: check relevant policy and help collect the necessary information.
    - Answer the questions as a resident with BSN 101177006
``` 

- Remove the Web search tool. Then go to Knowledge.

<img src="../images/image14.png" width="139px" alt="image14.png">

- Then select Foundry IQ.

<img src="../images/image15.png" width="277px" alt="image15.png">

- Select the knowledge base: vergunning-beleid-knowledgebase (permit policy knowledge base).

<img src="../images/image16.png" width="275px" alt="image16.png">

- Once the knowledge datasource is linked, you can ask questions. Because this is linked as a tool, Foundry first asks for permission to use the tool. Example questions: “What is the parking policy in zone A?” and “I want to throw away a fridge: what should I do?”

<img src="../images/image17.png" width="391px" alt="image17.png">

## What is Foundry IQ?

Foundry IQ is an agentic RAG solution (Retrieval-Augmented Generation). Foundry IQ is intended for unstructured data, think of documents with policies, processes and user information. This allows an agent to retrieve information from multiple linked sources and use that context to generate an answer. Foundry IQ forms in practice a link from Foundry to Azure AI Search and knowledge bases.

Instead of one separate knowledge base, you can connect multiple sources in Azure AI Search (for example documents/SharePoint, data sources or other repositories). The agent then specifically searches in these sources via a language model. The language model selects relevant passages and combines them into a complete and consistent answer (traceable to the used sources where possible).

The knowledge base vergunning-beleid-knowledgebase consists of the following sources:

- Waste information (scraped from the web), including permit information from a municipality website.
- A data source indexed by Fabric with Contoso policy rules.

<img src="../images/image18.png" alt="image18.png">

 To make these knowledge bases possible within Microsoft Foundry, you have received read rights and the Index Reader role as AI User. In the Azure portal you can also view the knowledge bases via the link below.

[https://portal.azure.com/#@overheidcontoso.nl/resource/subscriptions/48022148-dab0-48d2-8577-70c13def7ad0/resourceGroups/rg-foundry-mun/providers/Microsoft.Search/searchServices/mun-srch-foundry-dev/knowledgeBases](https://portal.azure.com/)

## 👣 Step 2: Using Tools. Requests -MCP

- Choose Save to save your changes.
- Then we use a pre-configured tool via Tools.

Go to Tools and select aanvragen-mcp.

<img src="../images/image19.png" width="583px" alt="image19.png">

- Now ask a question about open requests: Which requests do I have open?

<img src="../images/image20.png" alt="image20.png">

Try a report (for example something that is broken) or apply for a parking permit via the agent.

- Also view traces and monitor and enable continuous evaluations on groundedness and Intent.

<img src="../images/image21.png" alt="image21.png">

**End of Lab 3**

This was the last lab and with this we close the Agent Lab.

Please let us know if you have any questions. If you finish quickly, feel free to experiment further by asking other and more complex questions.

### [Back to readme](./README.md)
