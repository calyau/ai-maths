---
concept: "Mycielski's Construction"
slug: mycielski-construction
category: graph-colouring
subcategory: vertex-colouring
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: "5.2 Colouring vertices"
extraction_confidence: medium
aliases:
  - "Mycielskian"
prerequisites:
  - chromatic-number
extends: []
related:
  - erdos-girth-chromatic
contrasts_with: []
answers_questions:
  - "How can triangle-free graphs with large chromatic number be explicitly constructed?"
---

# Quick Definition
Mycielski's construction provides an explicit way to build triangle-free graphs of arbitrarily large chromatic number, complementing Erdos's non-constructive existence proof.

# Core Definition
Exercise 23 asks to construct, for every k, a triangle-free k-chromatic graph. This can be done via Mycielski's construction (or Zykov's construction), which iteratively builds larger triangle-free graphs with increasing chromatic number.

# Prerequisites
- **Chromatic number**

# Key Properties
1. Produces triangle-free graphs with chi = k for any k
2. Constructive (unlike Erdos's probabilistic proof)
3. The resulting graphs have girth 4 (triangle-free but contain C_4)

# Context & Application
This construction provides concrete examples demonstrating that chi and omega can be far apart: omega = 2 (triangle-free) while chi is arbitrarily large.

# Relationships
## Related
- **Erdos's theorem** -- Non-constructive proof of the same phenomenon

# Source Reference
Chapter 5, Exercise 23, page 135.

# Verification Notes
- Referenced in Exercise 23
- Confidence: MEDIUM -- exercise reference
