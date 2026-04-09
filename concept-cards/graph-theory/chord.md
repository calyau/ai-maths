---
concept: Chord
slug: chord

category: paths-and-cycles
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 17
section: "1.3 Paths and cycles"

extraction_confidence: high

aliases: []

prerequisites:
  - cycle
  - edge
extends: []
related:
  - induced-cycle
contrasts_with: []

answers_questions:
  - "What is a chord of a cycle?"
  - "What is an induced cycle?"
---

# Quick Definition
A chord of a cycle is an edge that joins two vertices of the cycle but is not itself an edge of the cycle. An induced cycle is one with no chords.

# Core Definition
An edge which joins two vertices of a cycle but is not itself an edge of the cycle is a chord of that cycle. Thus, an induced cycle in G, a cycle in G forming an induced subgraph, is one that has no chords (Diestel, p. 8).

# Prerequisites
- **Cycle** — chords are defined relative to cycles
- **Edge** — a chord is an edge

# Key Properties
1. A chord connects two non-adjacent (in the cycle) vertices of the cycle
2. An induced cycle (chordless cycle) has no chords
3. Adding a chord to a cycle creates two shorter cycles

# Examples
**Example** (p. 8): Fig. 1.3.3 shows a cycle C^8 with chord xy, and induced cycles C^6 and C^4.

# Relationships
## Builds Upon
- **cycle**, **edge**

## Related
- **induced-cycle** — a cycle without chords

# Source Reference
Chapter 1: The Basics, Section 1.3, page 8 (pdf p. 18). See Fig. 1.3.3.

# Verification Notes
- Direct from p. 8
- Confidence: HIGH
