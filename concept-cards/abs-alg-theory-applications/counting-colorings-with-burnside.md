---
concept: Counting Colorings with Burnside's Theorem
slug: counting-colorings-with-burnside
category: group-structure
subcategory: applications
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Group Actions"
chapter_number: 14
pdf_page: 186
section: "Burnside's Counting Theorem"
extraction_confidence: high
aliases: []
prerequisites:
  - burnside-counting-theorem
  - group-action
extends:
  - burnside-counting-theorem
related:
  - symmetry-group
contrasts_with: []
answers_questions:
  - "How do I count distinct colorings up to symmetry?"
---

# Quick Definition

To count distinct colorings of a figure using $|Y|$ colors under a symmetry group $G$, use Burnside's theorem with Proposition 14.21: if $\sigma$ has $n$ cycles in its decomposition, then $|\widetilde{X}_\sigma| = |Y|^n$.

# Core Definition

**Proposition 14.21**: "Let $G$ be a permutation group of $X$ and $\widetilde{X}$ the set of functions from $X$ to $Y$. Then there exists a permutation group $\widetilde{G}$ acting on $\widetilde{X}$... Furthermore, if $n$ is the number of cycles in the cycle decomposition of $\sigma$, then $|\widetilde{X}_\sigma| = |Y|^n$" (Judson, p. 188).

# Prerequisites

- **Burnside's counting theorem** — The main counting tool
- **Group action** — Symmetry group acts on colorings

# Key Properties

1. For each $\sigma \in G$, count cycles in cycle decomposition
2. $|\widetilde{X}_\sigma| = |Y|^{(\text{number of cycles})}$
3. Number of distinct colorings = $\frac{1}{|G|} \sum_{\sigma \in G} |Y|^{c(\sigma)}$ where $c(\sigma)$ is the cycle count

# Examples

**Example 1** (p. 186-188): Coloring 4 vertices of a square with 2 colors, $G = D_4$: identity has 4 cycles, each rotation/reflection has fewer. Result: 6 colorings.

**Example 2** (p. 188): Coloring with 4 colors: $\frac{1}{8}(4^4 + 4^1 + 4^2 + 4^1 + 4^2 + 4^2 + 4^3 + 4^3) = 55$.

# Relationships

## Builds Upon
- **Burnside's counting theorem** — Core technique

## Related
- **Symmetry group** — The group acting on the object

# Source Reference

Chapter 14: Group Actions, Section 14.3, pages 186-188. Proposition 14.21.

# Verification Notes

- Definition source: Proposition 14.21
- Confidence: HIGH
