---
# === CORE IDENTIFICATION ===
concept: Proper Subgroup
slug: proper-subgroup

# === CLASSIFICATION ===
category: group-theory
subcategory: group-definitions
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Groups"
chapter_number: 3
pdf_page: 51
section: "Subgroups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - subgroup
extends: []
related:
  - trivial-subgroup
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a subgroup?"
---

# Quick Definition

A proper subgroup of a group $G$ is a subgroup that is a proper subset of $G$; that is, it is a subgroup $H$ with $H \neq G$.

# Core Definition

"A subgroup that is a proper subset of $G$ is called a proper subgroup" (Judson, p. 51).

# Prerequisites

- **Subgroup** — A proper subgroup is a special case

# Key Properties

1. $H \subset G$ and $H \neq G$
2. Every group with at least two elements has at least two subgroups: $\{e\}$ and $G$ itself

# Context & Application

Proper subgroups are important for understanding group structure. Groups where every proper subgroup is cyclic have special properties. Comparing the number and structure of proper subgroups can distinguish non-isomorphic groups.

# Examples

**Example 1** (p. 52): $\{0, 2\}$ is the only nontrivial proper subgroup of $\mathbb{Z}_4$.

**Example 2** (p. 52): $\mathbb{Z}_2 \times \mathbb{Z}_2$ has three nontrivial proper subgroups: $\{(0,0),(0,1)\}$, $\{(0,0),(1,0)\}$, and $\{(0,0),(1,1)\}$.

# Relationships

## Builds Upon
- **subgroup** — Is a subgroup

## Related
- **trivial-subgroup** — $\{e\}$ is a proper subgroup when $|G| > 1$

# Source Reference

Chapter 3: Groups, Section 3.3, page 51.

# Verification Notes

- Definition source: Direct from p. 51
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
