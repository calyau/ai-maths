---
# === CORE IDENTIFICATION ===
concept: Coset Partition Theorem
slug: coset-partition-theorem

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
  - coset-equality-conditions
extends: []
related:
  - lagranges-theorem
  - index-of-a-subgroup
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Do cosets partition a group?"
  - "Can two distinct cosets overlap?"
---

# Quick Definition

The left cosets of a subgroup $H$ in a group $G$ partition $G$ into disjoint subsets of equal size. Any two left cosets are either identical or completely disjoint.

# Core Definition

**Theorem 6.4:** "Let $H$ be a subgroup of a group $G$. Then the left cosets of $H$ in $G$ partition $G$. That is, the group $G$ is the disjoint union of the left cosets of $H$ in $G$" (Judson, p. 88). The same holds for right cosets (Remark 6.5).

# Prerequisites

- **Left Coset** — The objects being partitioned
- **Coset Equality Conditions** — Used in the proof

# Key Properties

1. $G$ is the disjoint union of the left cosets of $H$
2. Two cosets are either identical or have empty intersection
3. Each coset has exactly $|H|$ elements (Proposition 6.9)
4. Right cosets also partition $G$ (Remark 6.5)

# Construction / Recognition

## To Verify:
1. Show that every element of $G$ belongs to some coset (trivially, $g \in gH$)
2. Show that if $g_1H \cap g_2H \neq \emptyset$, then $g_1H = g_2H$

# Context & Application

This partition property is the key step in proving Lagrange's Theorem: since $G$ is partitioned into $[G:H]$ cosets each of size $|H|$, we get $|G| = [G:H] \cdot |H|$.

# Examples

**Example 1** (p. 87): In $\mathbb{Z}_6$ with $H = \{0, 3\}$, the three cosets $\{0,3\}$, $\{1,4\}$, $\{2,5\}$ partition $\mathbb{Z}_6$.

# Relationships

## Builds Upon
- **Left Coset** — The theorem is about left cosets
- **Coset Equality Conditions** — The proof uses Lemma 6.3

## Enables
- **Lagrange's Theorem** — Follows directly from this partition

# Common Errors

- **Error**: Trying to find elements that belong to two different cosets
  **Correction**: Impossible; cosets are disjoint or identical

# Common Confusions

- **Confusion**: Thinking cosets can partially overlap
  **Clarification**: Two cosets sharing even one element must be completely identical

# Source Reference

Chapter 6: Cosets and Lagrange's Theorem, Section 6.1, Theorem 6.4, page 88.

# Verification Notes

- Definition source: Direct from Theorem 6.4
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
