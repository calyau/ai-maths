---
concept: Well-Definedness of Coset Multiplication
slug: well-definedness-of-coset-multiplication
category: group-structure
subcategory: group-constructions
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Normal Subgroups and Factor Groups"
chapter_number: 10
pdf_page: 139
section: "Factor Groups and Normal Subgroups"
extraction_confidence: high
aliases: []
prerequisites:
  - normal-subgroup
  - coset
extends: []
related:
  - factor-group
contrasts_with: []
answers_questions:
  - "Why is normality needed for factor groups?"
  - "How do I construct a factor group?"
---

# Quick Definition

The coset multiplication $(aN)(bN) = abN$ in a factor group is well-defined only when $N$ is normal. Normality ensures the result is independent of the choice of coset representatives.

# Core Definition

In the proof of Theorem 10.4, Judson shows well-definedness: "This operation must be shown to be well-defined; that is, group multiplication must be independent of the choice of coset representative" (p. 139). If $aN = bN$ and $cN = dN$, then $a = bn_1$ and $c = dn_2$ for $n_1, n_2 \in N$. Using normality: $acN = bn_1dn_2N = bn_1dN = bn_1Nd = bNd = bdN$.

# Prerequisites

- **Normal subgroup** — Required for well-definedness
- **Coset** — Elements of the factor group

# Key Properties

1. Without normality, $(aN)(bN)$ may depend on representatives
2. The key step uses $n_1 d N = n_1 N d = N d = dN$ (normality)
3. Normality is both necessary and sufficient

# Context & Application

This is the crucial step in constructing factor groups. Understanding why normality is needed (and why arbitrary subgroups don't work) is essential for grasping the theory.

# Relationships

## Enables
- **Factor group** — Well-definedness is required for the group operation

# Source Reference

Chapter 10: Normal Subgroups and Factor Groups, Section 10.1, p. 139. Theorem 10.4 proof.

# Verification Notes

- Definition source: Theorem 10.4 proof
- Confidence: HIGH
