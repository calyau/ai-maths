---
# === CORE IDENTIFICATION ===
concept: Identity Mapping
slug: identity-mapping

# === CLASSIFICATION ===
category: foundations
subcategory: set-theory
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Preliminaries"
chapter_number: 1
pdf_page: 23
section: "Cartesian Products and Mappings"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - identity function
  - identity map

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mapping
extends:
  - mapping
related:
  - inverse-mapping
  - identity-element-uniqueness
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

The identity mapping on a set $S$, denoted $\text{id}_S$, is the map that sends every element to itself: $\text{id}(s) = s$ for all $s \in S$.

# Core Definition

"If $S$ is any set, we will use $\text{id}_S$ or $\text{id}$ to denote the identity mapping from $S$ to itself. Define this map by $\text{id}(s) = s$ for all $s \in S$" (Judson, p. 23).

# Prerequisites

- **Mapping** — The identity mapping is a particular function

# Key Properties

1. $\text{id}_S \circ f = f$ for any $f: A \to S$
2. $f \circ \text{id}_A = f$ for any $f: A \to B$
3. The identity mapping is always bijective
4. It serves as the identity element in groups of permutations

# Construction / Recognition

## To Construct:
1. For every element $s \in S$, set $\text{id}(s) = s$

# Context & Application

The identity mapping is the identity element in any group of functions under composition, including permutation groups and symmetry groups. In the symmetry group $S_3$, the identity is denoted $\text{id}$.

# Examples

**Example 1** (p. 23): For any set $S$, the identity mapping $\text{id}_S(s) = s$ for all $s \in S$.

# Relationships

## Builds Upon
- **mapping** — The identity mapping is a specific function

## Enables
- **inverse-mapping** — Defined as $g \circ f = \text{id}_A$ and $f \circ g = \text{id}_B$
- **group** — Identity element in permutation/symmetry groups

## Related
- **identity-element-uniqueness** — The identity mapping corresponds to the group identity

# Common Confusions

- **Confusion**: Thinking the identity mapping does "nothing" and is trivial
  **Clarification**: While simple, it plays the essential role of identity element in function groups

# Source Reference

Chapter 1: Preliminaries, Section 1.2, page 23.

# Verification Notes

- Definition source: Direct quote from p. 23
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
