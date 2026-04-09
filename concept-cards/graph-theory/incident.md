---
concept: Incident
slug: incident

category: graph-fundamentals
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 11
section: "1.1 Graphs"

extraction_confidence: high

aliases:
  - "incidence"

prerequisites:
  - graph
  - vertex
  - edge
extends: []
related:
  - adjacent
  - endvertex
  - degree
contrasts_with:
  - adjacent

answers_questions:
  - "What does it mean for a vertex to be incident with an edge?"
---

# Quick Definition
A vertex v is incident with an edge e if v is one of the endpoints of e (i.e., v is an element of e).

# Core Definition
A vertex v is incident with an edge e if v is in e; then e is an edge at v. The two vertices incident with an edge are its endvertices or ends, and an edge joins its ends (Diestel, p. 3).

# Prerequisites
- **Graph**, **vertex**, **edge** — incidence is a relation between vertices and edges

# Key Properties
1. Each edge is incident with exactly two vertices (its ends)
2. Each vertex is incident with zero or more edges
3. The set of all edges incident with a vertex v is denoted E(v)

# Construction / Recognition
To check incidence: vertex v is incident with edge e = xy if and only if v = x or v = y.

# Context & Application
Incidence is the fundamental relation between vertices and edges. It contrasts with adjacency, which is a relation between two vertices or two edges.

# Examples
**Example** (p. 2-3): In the edge e = {1, 5}, vertex 1 is incident with e and vertex 5 is incident with e.

# Relationships
## Builds Upon
- **graph**, **vertex**, **edge**

## Enables
- **degree** — counts edges incident with a vertex

## Contrasts With
- **adjacent** — adjacency is between two vertices or two edges; incidence is between a vertex and an edge

# Common Confusions
- **Confusion**: Confusing incidence with adjacency
  **Clarification**: Incidence relates a vertex to an edge; adjacency relates two vertices (or two edges) to each other

# Source Reference
Chapter 1: The Basics, Section 1.1, page 3 (pdf p. 13).

# Verification Notes
- Direct from p. 3
- Confidence: HIGH
