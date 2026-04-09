---
# === CORE IDENTIFICATION ===
concept: Trivial Subgroup
slug: trivial-subgroup

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
  - proper-subgroup
contrasts_with:
  - proper-subgroup

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a subgroup?"
---

# Quick Definition

The trivial subgroup of a group $G$ is the subgroup $H = \{e\}$ containing only the identity element.

# Core Definition

"The subgroup $H = \{e\}$ of a group $G$ is called the trivial subgroup" (Judson, p. 51). Every group has this subgroup.

# Prerequisites

- **Subgroup** — The trivial subgroup is a specific subgroup

# Key Properties

1. Contains exactly one element: the identity
2. Is a subgroup of every group
3. Is always abelian (trivially)
4. Is always cyclic (trivially)

# Context & Application

The trivial subgroup appears as a base case in many proofs about subgroups and is one of the two subgroups every group possesses (the other being the group itself).

# Examples

**Example 1** (p. 51): In any group $G$, $\{e\}$ is a subgroup since $e \cdot e = e$, $e^{-1} = e$, and $e$ is the identity.

# Relationships

## Builds Upon
- **subgroup** — Is a subgroup

## Contrasts With
- **proper-subgroup** — The trivial subgroup is the smallest proper subgroup (when $|G| > 1$)

# Source Reference

Chapter 3: Groups, Section 3.3, page 51.

# Verification Notes

- Definition source: Direct from p. 51
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
