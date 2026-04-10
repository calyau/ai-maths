---
concept: Erdős-Szekeres Theorem on Cups and Caps
slug: erdos-szekeres-cups-and-caps
category: ramsey-theory
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 190
section: "VI.1 The Fundamental Ramsey Theorems"
extraction_confidence: high
aliases:
  - "Theorem VI.3"
  - "Erdős-Szekeres theorem"
  - "cups and caps theorem"
prerequisites:
  - ramsey-theorem-finite
extends: []
related:
  - convex-polygon-problem
contrasts_with: []
answers_questions:
  - "What is the Erdős-Szekeres theorem on cups and caps?"
---

# Quick Definition
Every non-degenerate set of C(k+ℓ−4, k−2) + 1 points in the plane contains a k-cup (convex k-set) or an ℓ-cap (concave ℓ-set). This bound is tight.

# Core Definition
**Theorem 3** (Bollobás, p. 190): For k, ℓ ≥ 2, every non-degenerate set of C(k+ℓ−4, k−2) + 1 points contains a k-cup or an ℓ-cap. Furthermore, for all k, ℓ ≥ 2, there exists a non-degenerate set of C(k+ℓ−4, k−2) points containing neither a k-cup nor an ℓ-cap.

A k-cup is a set of k points (x_i, h(x_i)) where h is convex; a k-cap is analogous with concave h. Equivalently, a k-cup has non-decreasing slopes and a k-cap has non-increasing slopes.

# Prerequisites
- **Ramsey theorem (finite)** — the theorem is Ramsey-like in structure

# Key Properties
1. The threshold is exactly C(k+ℓ−4, k−2) + 1 (tight)
2. The proof is by double induction on k and ℓ
3. Implies every set of C(2k−4, k−2) + 1 points in general position contains a convex k-gon
4. Erdős-Szekeres conjecture: 2^{k−2} + 1 points suffice for a convex k-gon

# Context & Application
This theorem connects Ramsey theory to combinatorial geometry. The Erdős-Szekeres conjecture about convex k-gons (the "happy ending problem") remains one of the most famous open problems in combinatorial geometry.

# Examples
**Example** (p. 191): Every set of C(2k−4, k−2) + 1 points in general position contains a convex k-gon.

# Relationships
## Related
- **Ramsey theorem** — structural analogue
- **Convex polygon problem** — direct application

# Source Reference
Chapter VI: Ramsey Theory, Section VI.1, Theorem 3, pages 190–192.

# Verification Notes
- Definition source: Direct theorem statement from p. 190
- Confidence rationale: Explicit theorem with both parts proved
- Uncertainties: None
- Cross-reference status: Verified
