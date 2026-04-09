---
# === CORE IDENTIFICATION ===
concept: Coset Equality Conditions
slug: coset-equality-conditions

# === CLASSIFICATION ===
category: group-structure
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Cosets and Lagrange's Theorem"
chapter_number: 6
pdf_page: 88
section: "6.1 Cosets"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - left-coset
  - right-coset
extends: []
related:
  - lagranges-theorem
  - index-of-a-subgroup
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When are two cosets equal?"
  - "How do I determine if two elements are in the same coset?"
---

# Quick Definition

Two left cosets $g_1H$ and $g_2H$ are equal if and only if $g_1^{-1}g_2 \in H$. This lemma provides five equivalent conditions for coset equality and is fundamental to working with cosets.

# Core Definition

**Lemma 6.3** (Judson, p. 88): Let $H$ be a subgroup of a group $G$ and suppose that $g_1, g_2 \in G$. The following conditions are equivalent:
1. $g_1H = g_2H$
2. $Hg_1^{-1} = Hg_2^{-1}$
3. $g_1H \subseteq g_2H$
4. $g_2 \in g_1H$
5. $g_1^{-1}g_2 \in H$

# Prerequisites

- **Left Coset** — These conditions characterize when left cosets are equal
- **Right Coset** — Condition 2 relates to right cosets

# Key Properties

1. Coset equality is transitive, symmetric, and reflexive (it defines an equivalence relation)
2. Any element of a coset can serve as its representative
3. Two cosets are either identical or completely disjoint (Theorem 6.4)
4. Condition 5 ($g_1^{-1}g_2 \in H$) is often the most practical test

# Construction / Recognition

## To Test if $g_1H = g_2H$:
1. Compute $g_1^{-1}g_2$
2. Check if the result is in $H$
3. If yes, the cosets are equal; if no, they are disjoint

# Context & Application

These conditions are used throughout group theory for computing with cosets, proving Lagrange's theorem, and determining the index of subgroups.

# Examples

**Example 1** (p. 87-88): In $S_3$ with $H = \{(1), (123), (132)\}$: $(12)H = (13)H$ because $(12)^{-1}(13) = (12)(13) = (132) \in H$.

# Relationships

## Builds Upon
- **Left Coset** — These are conditions for left coset equality

## Enables
- **Lagrange's Theorem** — Coset partition property follows from these conditions

# Common Errors

- **Error**: Checking $g_1g_2^{-1} \in H$ instead of $g_1^{-1}g_2 \in H$ for left cosets
  **Correction**: For left cosets, the correct test is $g_1^{-1}g_2 \in H$

# Common Confusions

- **Confusion**: Thinking that if $g_1H \cap g_2H \neq \emptyset$ then $g_1H$ and $g_2H$ merely overlap
  **Clarification**: If they share any element, they are completely identical

# Source Reference

Chapter 6: Cosets and Lagrange's Theorem, Section 6.1, Lemma 6.3, page 88.

# Verification Notes

- Definition source: Direct from Lemma 6.3, p. 88
- Confidence rationale: Explicit lemma with five equivalent conditions
- Uncertainties: None
- Cross-reference status: Verified
