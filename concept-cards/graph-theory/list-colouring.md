---
concept: List Colouring
slug: list-colouring
category: graph-colouring
subcategory: list-colouring
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: "5.4 List colouring"
extraction_confidence: high
aliases:
  - "list coloring"
  - "choosability"
  - "colouring from lists"
prerequisites:
  - vertex-colouring
extends:
  - vertex-colouring
related:
  - choice-number
  - list-chromatic-index
  - thomassen-five-choosable
contrasts_with:
  - vertex-colouring
answers_questions:
  - "What is list colouring?"
  - "What distinguishes list colouring from ordinary colouring?"
---

# Quick Definition
In list colouring, each vertex v has its own list S_v of permitted colours. A graph is k-choosable if it can be properly coloured from any assignment of lists of size k. The minimum such k is the choice number ch(G).

# Core Definition
"Let (S_v)_{v in V} be a family of sets. We call a vertex colouring c of G with c(v) in S_v for all v a colouring from the lists S_v. The graph G is called k-list-colourable, or k-choosable, if, for every family (S_v) with |S_v| = k for all v, there is a vertex colouring of G from the lists S_v. The least integer k for which G is k-choosable is the list-chromatic number, or choice number ch(G)" (Diestel, p. 121).

# Prerequisites
- **Vertex colouring** -- List colouring generalizes ordinary colouring

# Key Properties
1. ch(G) >= chi(G) (list colouring is harder than ordinary colouring)
2. Ordinary colouring is the special case where all lists equal {1,...,k}
3. Many upper bounds for chi also hold for ch (Brooks' theorem, Proposition 5.2.2)
4. chi and ch can be far apart (Exercise 25)
5. Planar graphs are 5-choosable (Thomassen's theorem)
6. Planar graphs are NOT always 4-choosable

# Context & Application
List colouring, introduced by Vizing in 1976, generalizes ordinary colouring by allowing different available colours at different vertices. Paradoxically, proving ch(G) <= k can sometimes be EASIER than proving chi(G) <= k, because the variable list lengths provide more structure for inductive arguments. Thomassen's proof that planar graphs are 5-choosable exemplifies this phenomenon.

# Relationships
## Builds Upon
- **Vertex colouring** -- Generalization

## Enables
- **Choice number** -- The main invariant
- **Thomassen's theorem** -- Planar graphs are 5-choosable

## Contrasts With
- **Vertex colouring** -- Ordinary colouring uses a single global set of colours

# Common Confusions
- **Confusion**: Thinking ch(G) = chi(G) always
  **Clarification**: ch(G) >= chi(G) always, but the gap can be arbitrarily large. However, for bipartite edge colouring they coincide (Galvin).

# Source Reference
Chapter 5, Section 5.4, pages 121-126.

# Verification Notes
- Definition quoted from p. 121
- Confidence: HIGH -- explicit definition
