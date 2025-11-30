Template for creating and submitting MAT496 capstone project.

# Overview of MAT496

In this course, we have primarily learned Langgraph. This is helpful tool to build apps which can process unstructured `text`, find information we are looking for, and present the format we choose. Some specific topics we have covered are:

- Prompting
- Structured Output 
- Semantic Search
- Retreaval Augmented Generation (RAG)
- Tool calling LLMs & MCP
- Langgraph: State, Nodes, Graph

We also learned that Langsmith is a nice tool for debugging Langgraph codes.

------

# Capstone Project objective

The first purpose of the capstone project is to give a chance to revise all the major above listed topics. The second purpose of the capstone is to show your creativity. Think about all the problems which you can not have solved earlier, but are not possible to solve with the concepts learned in this course. For example, We can use LLM to analyse all kinds of news: sports news, financial news, political news. Another example, we can use LLMs to build a legal assistant. Pretty much anything which requires lots of reading, can be outsourced to LLMs. Let your imagination run free.


-------------------------

# Project report Template

## Title: Personal Finance Mistake Detector AI

## Overview

This project implements an AI assistant that helps users detect mistakes in their personal finance habits. The assistant takes inputs such as income, expenses, savings, and investments, and identifies common financial mistakes such as low savings rate, absence of emergency fund, overspending, or poor investment distribution. It also generates a financial health score and allows users to simulate what-if scenarios to see how changes in their financial behavior impact their overall financial well-being. The system is built using LangGraph, structured prompting, retrieval-augmented generation (RAG), and tool calling.


## Reason for picking up this project

I picked this project because it closely aligns with both my academic interest in finance and the core concepts taught in this course. Through this project, I am able to apply structured prompting, tool calling for numerical financial computations, semantic search, retrieval-augmented generation (RAG), and LangGraph for building a multi-step AI workflow. The project demonstrates how large language models can be used beyond simple chat systems, to build an intelligent decision-support system in the domain of personal finance, which directly reflects the objectives of this course.


## Video Summary Link: 

Make a short -  3-5 min video of yourself, put it on youtube/googledrive, and put its link in your README.md.

- you can use this free tool for recording https://screenrec.com/
- Video format should be like this:
- your face should be visible
- State the overall job of your agent: what inputs it takes, and what output it gives.
- Very quickly, explain how your agent acts on the input and spits out the output. 
- show an example run of the agent in the video


## Plan

## Plan

The project was implemented in the following stages:

1. Collected and prepared a small personal finance knowledge base including budgeting rules, savings guidelines, and emergency fund norms.
2. Designed the input schema to collect user income, expenses, and savings through a conversational interface.
3. Implemented the core financial mistake detection logic using numerical calculations for savings rate, expense-to-income ratio, and emergency fund adequacy.
4. Integrated retrieval-based explanations using the knowledge base to justify detected mistakes and recommendations.
5. Designed and implemented the financial health score module.
6. Implemented the what-if scenario simulation module to test changes in income, expenses, and savings.
7. Built the multi-step assistant workflow using a structured control flow.
8. Tested the system on multiple user profiles and documented the results.



## Conclusion:

This project successfully implements an AI-based personal finance mistake detector that analyzes user income, expenses, and savings to generate a financial health score, detect financial risks, and provide actionable recommendations. The assistant also supports what-if simulations to help users understand how changes in spending and saving behavior affect their financial health. The project demonstrates the effective use of structured prompting, knowledge-based reasoning, and multi-step decision workflows for real-world financial applications.


----------

# Added instructions:

- This is a `solo assignment`. Each of you will work alone. You are free to talk, discuss with chatgpt, but you are responsible for what you submit. Some students may be called for viva. You should be able to each and every line of work submitted by you.

- `commit` History maintenance.
  - Fork this repository and build on top of that.
  - For every step in your plan, there has to be a commit.
  - Change [TODO] to [DONE] in the plan, before you commit after that step. 
  - The commit history should show decent amount of work spread into minimum two dates. 
  - **All the commits done in one day will be rejected**. Even if you are capable of doing the whole thing in one day, refine it in two days.  
 
 - Deadline: Dec 2nd, Tuesday 11:59 pm


# Grading: total 25 marks

- Coverage of most of topics in this class: 20
- Creativity: 5
  
