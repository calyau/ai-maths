---
concept: Exceptional Set
slug: exceptional-set
category: extremal-graph-theory
subcategory: regularity
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Extremal Graph Theory"
chapter_number: 7
pdf_page: 186
section: "7.4 Szemeredi's regularity lemma"
extraction_confidence: high
aliases:
  - "V_0"
prerequisites:
  - epsilon-regular-partition
related:
  - regularity-lemma
answers_questions:
  - "What is the exceptional set in a regular partition?"
---

# Quick Definition
The exceptional set V_0 in an epsilon-regular partition is a small set (|V_0| <= epsilon*|V|) containing leftover vertices that allow the remaining sets to have exactly equal size.

# Core Definition
In an epsilon-regular partition {V_0, V_1, ..., V_k}, the set V_0 is the **exceptional set**. It may be empty. Its size is bounded by epsilon*|V|. Vertices in V_0 are disregarded when assessing the uniformity of the partition. (Diestel, p. 176-177)

# Prerequisites
- **Epsilon-regular partition** — The exceptional set is part of the partition

# Key Properties
1. |V_0| <= epsilon*|V|
2. May be empty
3. Exists for convenience: allows equal-sized non-exceptional parts
4. Vertices in V_0 are not involved in regularity conditions

# Source Reference
Chapter 7, Section 7.4, pages 176-177 (pdf pages 186-187).

# Verification Notes
- Confidence: HIGH — explicitly defined
