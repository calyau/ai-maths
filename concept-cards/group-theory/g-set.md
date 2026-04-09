---
# === CORE IDENTIFICATION ===
concept: G-Set
slug: g-set

# === CLASSIFICATION ===
category: group-actions
subcategory: definitions
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Groups Acting on Sets"
chapter_number: 4
pdf_page: 56
section: "Definition and examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - G-space

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-action
extends:
  - group-action
related:
  - g-map
  - homogeneous-g-set
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a G-set?"
---

# Quick Definition

A $G$-set is a set $X$ equipped with a left action of the group $G$.

# Core Definition

"A set together with a (left) action of $G$ is called a (left) $G$-set" (Milne, Definition 4.1, p. 56).

# Prerequisites

- **Group action** — A $G$-set is a set with a $G$-action

# Key Properties

1. A map of $G$-sets ($G$-map) is a map $\varphi: X \to Y$ with $\varphi(gx) = g\varphi(x)$
2. An isomorphism of $G$-sets is a bijective $G$-map
3. Every transitive $G$-set is isomorphic to $G/H$ for some subgroup $H$ (Proposition 4.7)

# Context & Application

$G$-sets provide the categorical framework for studying group actions. Morphisms of $G$-sets preserve the action structure.

# Examples

**Example 1** (p. 56): $\{1, 2, \ldots, n\}$ is an $S_n$-set.

**Example 2** (p. 56): $G/H$ is a $G$-set for any subgroup $H$.

# Relationships

## Builds Upon
- **group-action** — A $G$-set is a set with a group action

## Related
- **g-map** — Morphisms in the category of $G$-sets

# Source Reference

Chapter 4: Groups Acting on Sets, "Definition and examples", page 56.

# Verification Notes

- Definition source: Direct from Definition 4.1, p. 56
- Confidence: HIGH
- Uncertainties: None
