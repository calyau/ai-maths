---
# === CORE IDENTIFICATION ===
concept: Groups of Lie Type
slug: groups-of-lie-type

# === CLASSIFICATION ===
category: automorphisms-extensions
subcategory: classification
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Automorphisms and Extensions"
chapter_number: 3
pdf_page: 51
section: "A. The classification of finite simple groups"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - finite groups of Lie type

# === TYPED RELATIONSHIPS ===
prerequisites:
  - simple-group
  - classification-of-finite-simple-groups
extends: []
related:
  - sporadic-groups
contrasts_with:
  - sporadic-groups

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the groups of Lie type in the classification?"
---

# Quick Definition

Groups of Lie type are infinite families of finite simple groups arising as matrix groups over finite fields, forming the largest class in the classification.

# Core Definition

"Certain infinite families of matrix groups (said to be of Lie type)" (Milne, p. 51). The prototypical example is $\operatorname{PSL}_n(\mathbb{F}_q) = \operatorname{SL}_n(\mathbb{F}_q)/\{\text{centre}\}$, which is simple for $n \geq 3$ and for $n = 2$, $q > 3$.

# Prerequisites

- **Simple group** — Groups of Lie type are simple groups
- **Classification of finite simple groups** — They form class (c)

# Key Properties

1. By far the largest class of finite simple groups
2. Defined as quotients of matrix groups over finite fields $\mathbb{F}_q$
3. $\operatorname{PSL}_n(\mathbb{F}_q)$ is simple when $n \geq 3$ or $n = 2$, $q > 3$
4. Other families arise from the classical groups in (1.8) of Milne

# Examples

**Example 1** (p. 51): $\operatorname{PSL}_n(\mathbb{F}_q) = \operatorname{SL}_n(\mathbb{F}_q)/\{\text{scalar matrices}\}$.

**Example 2** (p. 52): $\operatorname{PSL}_3(\mathbb{F}_2)$ has order 168 and is the second smallest noncommutative simple group.

# Relationships

## Contrasts With
- **sporadic-groups** — Sporadic groups do not fit into infinite families

# Source Reference

Chapter 3: Automorphisms and Extensions, page 51.

# Verification Notes

- Definition source: Brief mention on p. 51
- Confidence: MEDIUM — only briefly described in source
- Uncertainties: Details referenced to other texts
