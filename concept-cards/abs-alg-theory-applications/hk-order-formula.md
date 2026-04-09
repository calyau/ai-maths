---
concept: HK Order Formula
slug: hk-order-formula
category: group-structure
subcategory: subgroup-counting
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "The Sylow Theorems"
chapter_number: 15
pdf_page: 200
section: "Examples and Applications"
extraction_confidence: high
aliases:
  - "product formula for subgroups"
  - "|HK| formula"
prerequisites:
  - subgroup
  - lagranges-theorem
extends: []
related:
  - second-isomorphism-theorem
  - sylow-p-subgroup
contrasts_with: []
answers_questions:
  - "How do I compute the order of a product of subgroups?"
---

# Quick Definition

For finite subgroups $H$ and $K$ of a group $G$, the order of the product set $HK$ is given by $|HK| = \frac{|H| \cdot |K|}{|H \cap K|}$.

# Core Definition

**Lemma 15.18**: "Let $H$ and $K$ be finite subgroups of a group $G$. Then $|HK| = \frac{|H| \cdot |K|}{|H \cap K|}$" (Judson, p. 200).

# Prerequisites

- **Subgroup** — $H$ and $K$ are subgroups
- **Lagrange's theorem** — Order relationships

# Key Properties

1. $HK = \{hk : h \in H, k \in K\}$ (need not be a subgroup)
2. $|HK| \leq |H| \cdot |K|$
3. Each element of $HK$ is represented $|H \cap K|$ times
4. $|HK| = |H| \cdot |K|$ when $H \cap K = \{e\}$

# Context & Application

This formula is used in the Sylow theory, particularly in proving that groups of certain orders (like 48) are not simple, by showing that two Sylow subgroups must have a large intersection.

# Examples

**Example 1** (p. 200): For groups of order 48 with two Sylow 2-subgroups $H, K$ of order 16: if $|H \cap K| \leq 4$, then $|HK| \geq 64 > 48$, contradiction. So $|H \cap K| = 8$.

# Relationships

## Enables
- **Proving non-simplicity** — Used to bound intersection sizes

## Related
- **Second isomorphism theorem** — Related structural result

# Source Reference

Chapter 15: The Sylow Theorems, Section 15.2, p. 200. Lemma 15.18.

# Verification Notes

- Definition source: Lemma 15.18
- Confidence: HIGH
