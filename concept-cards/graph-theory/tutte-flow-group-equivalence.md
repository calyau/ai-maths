---
concept: Tutte's Flow-Group Equivalence
slug: tutte-flow-group-equivalence
category: network-flows
subcategory: algebraic-flows
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 156
section: "6.3 Group-valued flows"
extraction_confidence: high
aliases:
  - "Corollary 6.3.2"
prerequisites:
  - h-flow
  - flow-polynomial
related:
  - k-flow
answers_questions:
  - "When do two groups yield the same flow existence?"
---

# Quick Definition
If H and H' are finite abelian groups of equal order, then G has an H-flow if and only if G has an H'-flow (Corollary 6.3.2). Flow existence depends only on group order.

# Core Definition
**Corollary 6.3.2**: If H and H' are two finite abelian groups of equal order, then G has an H-flow if and only if G has an H'-flow. This follows from the flow polynomial (Theorem 6.3.1): the number of H-flows is P(|H|-1), which depends only on |H|. (Diestel, p. 146)

# Prerequisites
- **H-flow** — The equivalence concerns existence of H-flows
- **Flow polynomial** — The polynomial whose values determine the count

# Key Properties
1. Flow existence is a property of group ORDER, not group STRUCTURE
2. Allows choosing the most convenient group for proofs (e.g., Z_2^2 instead of Z_4)
3. Reduces general H-flow questions to k-flow questions (via Theorem 6.3.3)

# Context & Application
This is the "fundamental implication" that allows algebraic flow theory to focus on k-flows rather than dealing with arbitrary groups.

# Relationships
## Builds Upon
- **Flow polynomial**

## Enables
- Free choice of group in existence proofs

# Source Reference
Chapter 6, Section 6.3, Corollary 6.3.2, page 146 (pdf page 156).

# Verification Notes
- Confidence: HIGH — corollary with clear proof
