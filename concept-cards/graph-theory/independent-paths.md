---
concept: Independent Paths
slug: independent-paths

category: paths-and-cycles
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 16
section: "1.3 Paths and cycles"

extraction_confidence: high

aliases:
  - "A-B path"
  - "H-path"

prerequisites:
  - path
extends: []
related:
  - k-connected
  - separator
contrasts_with: []

answers_questions:
  - "What are independent paths?"
  - "What is an A-B path?"
  - "What is an H-path?"
---

# Quick Definition
Two or more paths are independent if none of them contains an inner vertex of another. An A-B path starts in A and ends in B with no other vertex in A or B. An H-path is non-trivial and meets H exactly in its ends.

# Core Definition
Two or more paths are independent if none of them contains an inner vertex of another. Two a-b paths are independent if and only if a and b are their only common vertices.

Given sets A, B of vertices, P = x_0 ... x_k is an A-B path if V(P) intersection A = {x_0} and V(P) intersection B = {x_k}.

Given a graph H, P is an H-path if P is non-trivial and meets H exactly in its ends (Diestel, pp. 7-8).

# Prerequisites
- **Path** — independent paths are paths with a disjointness condition

# Key Properties
1. Independent paths share no inner vertices
2. A-B paths have their first end in A, last end in B, no other vertex in A or B
3. H-paths meet H only at their endpoints; the edge of an H-path of length 1 is never in H

# Context & Application
Independent paths are central to Menger's theorem (Chapter 3), which characterizes k-connectivity.

# Relationships
## Builds Upon
- **path**

## Related
- **k-connected** — Menger's theorem relates connectivity to independent paths

# Source Reference
Chapter 1: The Basics, Section 1.3, pages 7-8 (pdf pp. 17-18).

# Verification Notes
- Direct from pp. 7-8
- Confidence: HIGH
