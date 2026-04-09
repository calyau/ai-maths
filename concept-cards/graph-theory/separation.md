---
concept: Separation
slug: separation

category: connectivity
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 20
section: "1.4 Connectivity"

extraction_confidence: high

aliases:
  - "proper separation"

prerequisites:
  - graph
  - separator
extends: []
related:
  - k-connected
contrasts_with: []

answers_questions:
  - "What is a separation of a graph?"
---

# Quick Definition
A separation of G is an unordered pair {A, B} with A union B = V such that G has no edge between A minus B and B minus A. Its order is |A intersection B|.

# Core Definition
The unordered pair {A, B} is a separation of G if A union B = V and G has no edge between A minus B and B minus A. Clearly, the latter is equivalent to saying that A intersection B separates A from B. If both A minus B and B minus A are non-empty, the separation is proper. The number |A intersection B| is the order of the separation {A, B} (Diestel, p. 11).

# Prerequisites
- **Graph**, **separator** — a separation formalizes how a separator divides the graph

# Key Properties
1. A separation {A, B} has A union B = V(G)
2. The overlap A intersection B is the separator
3. The order of the separation is |A intersection B|
4. A proper separation has both sides non-empty after removing the overlap

# Context & Application
Separations formalize the structure created when removing a separator. They are used in the definition of k-connectivity and in Mader's theorem.

# Relationships
## Builds Upon
- **separator**

## Enables
- **k-connected** — k-connectivity prevents low-order proper separations

# Source Reference
Chapter 1: The Basics, Section 1.4, page 11 (pdf p. 21).

# Verification Notes
- Direct from p. 11
- Confidence: HIGH
