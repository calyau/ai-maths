---
concept: Linked Set
slug: linked-set
category: connectivity
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Connectivity"
chapter_number: 3
pdf_page: 80
section: "3.5 Linking pairs of vertices"
extraction_confidence: high
aliases:
  - "linked vertex set"
prerequisites:
  - graph
  - path
extends: []
related:
  - k-linked-graph
  - mengers-theorem
contrasts_with: []
answers_questions:
  - "What does it mean for a set of vertices to be linked?"
---

# Quick Definition
A set X of vertices is linked in G if for any pairing of X into pairs {s1,t1}, ..., {sl,tl}, there exist disjoint paths Pi = si...ti with no inner vertices in X.

# Core Definition
A set X is **linked** in G if whenever we pick distinct vertices s1, ..., sl, t1, ..., tl in X we can find disjoint paths P1, ..., Pl in G such that each Pi links si to ti and has no inner vertex in X (Diestel, p. 80).

# Prerequisites
- **Graph** — linked sets are defined in a graph
- **Path** — linking is by disjoint paths

# Key Properties
1. The paths must be vertex-disjoint
2. Inner vertices of paths must lie outside X
3. Any pairing of X must be achievable
4. If |G| >= 2k and every set of <= 2k vertices is linked, G is k-linked

# Context & Application
The concept of a linked set underlies k-linkedness. A graph is k-linked when every set of 2k vertices is linked.

# Examples
**Example**: In K_n, any set of at most n vertices is linked (since K_n is floor(n/2)-linked).

# Relationships
## Builds Upon
- **Graph**, **path**

## Enables
- **k-linked graph** — defined via linked sets

# Source Reference
Chapter 3, Section 3.5, p. 80 (pdf p. 80).

# Verification Notes
- Definition from p. 80
- Confidence: HIGH — explicitly defined
