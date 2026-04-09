---
concept: Three Arcs Lemma
slug: three-arcs-lemma
category: planar-graphs
subcategory: topological-prerequisites
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Planar Graphs"
chapter_number: 4
pdf_page: 94
section: "4.1 Topological prerequisites"
extraction_confidence: high
aliases:
  - "Lemma 4.1.2"
prerequisites:
  - arc
  - jordan-curve-theorem
extends:
  - jordan-curve-theorem
related:
  - face-boundary
contrasts_with: []
answers_questions:
  - "How many regions do three arcs between the same endpoints create?"
---

# Quick Definition
Three arcs P_1, P_2, P_3 between the same two endpoints, otherwise disjoint, divide R^2 into exactly three regions with frontiers P_1 U P_2, P_2 U P_3, and P_1 U P_3.

# Core Definition
**Lemma 4.1.2**: "Let P_1, P_2, P_3 be three arcs, between the same two endpoints but otherwise disjoint. (i) R^2 \ (P_1 U P_2 U P_3) has exactly three regions, with frontiers P_1 U P_2, P_2 U P_3 and P_1 U P_3. (ii) If P is an arc between a point in P_1 and a point in P_3 whose interior lies in the region of R^2 \ (P_1 U P_3) that contains P_2, then P meets P_2" (Diestel, p. 85).

# Prerequisites
- **Arc**, **Jordan Curve Theorem**

# Key Properties
1. Three arcs create three regions
2. An arc connecting P_1 to P_3 through the region containing P_2 must cross P_2
3. Used in proofs about face structure and non-planarity

# Context & Application
This lemma is the technical tool behind many arguments in Chapter 4, including the proof that plane triangulations are maximal (Proposition 4.2.8) and parts of the Kuratowski theorem proof.

# Relationships
## Builds Upon
- **Jordan Curve Theorem**

## Enables
- **Plane triangulation** characterization
- **Kuratowski's theorem** proof (3-connected case)

# Source Reference
Chapter 4, Section 4.1, Lemma 4.1.2, page 85.

# Verification Notes
- Lemma from p. 85
- Confidence: HIGH
