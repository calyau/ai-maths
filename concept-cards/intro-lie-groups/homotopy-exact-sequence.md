---
# === CORE IDENTIFICATION ===
concept: Homotopy Exact Sequence for Lie Groups
slug: homotopy-exact-sequence

# === CLASSIFICATION ===
category: lie-groups
subcategory: homogeneous-spaces
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups: Basic Definitions"
chapter_number: 2
pdf_page: 11
section: "2.1"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "long exact sequence of homotopy groups"
  - "Corollary 2.11"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - coset-space
  - fiber-bundle
extends: []
related:
  - connected-component-of-identity
  - universal-cover-of-lie-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do the classical groups relate to each other?"
---

# Quick Definition

For a fiber bundle $H \to G \to G/H$, the long exact sequence $\pi_2(G/H) \to \pi_1(H) \to \pi_1(G) \to \pi_1(G/H) \to \{1\}$ relates the topology of $G$, $H$, and $G/H$.

# Core Definition

**Corollary 2.11** (Kirillov):
1. If $H$ is connected, then $\pi_0(G) = \pi_0(G/H)$.
2. If $G, H$ are connected, there is an exact sequence: $\pi_2(G/H) \to \pi_1(H) \to \pi_1(G) \to \pi_1(G/H) \to \{1\}$.

# Prerequisites

- **Coset space** — provides the base of the fiber bundle
- **Fiber bundle** — the exact sequence comes from the fiber bundle structure

# Key Properties

1. If $H$ is connected, connectedness of $G$ is equivalent to connectedness of $G/H$.
2. Used inductively with fiber bundles like $\mathrm{SO}(n-1) \to \mathrm{SO}(n) \to S^{n-1}$.
3. The key tool for computing $\pi_0$ and $\pi_1$ of classical groups.

# Construction / Recognition

## To Construct/Create:
1. Given a Lie subgroup $H \subset G$, form the fiber bundle $H \to G \to G/H$.
2. Apply the long exact sequence of homotopy groups.

## To Identify/Recognize:
1. Any computation of $\pi_0$ or $\pi_1$ of classical groups using fiber bundles.

# Context & Application

This is the primary tool for filling in the topological tables ($\pi_0$, $\pi_1$) of classical groups on pp. 16-17.

# Examples

**Example** (Exercise 2.8): Using $\mathrm{SU}(n-1) \to \mathrm{SU}(n) \to S^{2n-1}$ and $\pi_1(S^{2n-1}) = 0$ for $n \geq 2$: $\pi_1(\mathrm{SU}(n)) = \pi_1(\mathrm{SU}(n-1))$. Since $\mathrm{SU}(1) = \{1\}$, $\pi_1(\mathrm{SU}(n)) = \{1\}$ for all $n$.

**Example**: Using $\mathrm{SO}(n-1) \to \mathrm{SO}(n) \to S^{n-1}$: for $n \geq 3$, $\pi_1(\mathrm{SO}(n)) = \pi_1(\mathrm{SO}(3)) = \mathbb{Z}_2$.

# Relationships

## Builds Upon
- **Fiber bundle** — the exact sequence is associated to the bundle

## Enables
- **Topological classification of classical groups** — the tables on pp. 16-17

## Related
- **Universal cover** — $\pi_1$ determines the universal cover

# Common Errors

- **Error**: Forgetting the $\pi_2(G/H)$ term.
  **Correction**: When $G/H = S^{n-1}$ with $n \geq 3$, $\pi_2(S^{n-1}) = 0$ so it drops out. But for $n = 2$, $\pi_2(S^1) = 0$ also. Careful analysis is needed.

# Common Confusions

- **Confusion**: Whether $\pi_1(G)$ is always abelian for Lie groups.
  **Clarification**: Yes, $\pi_1(G)$ is abelian for any connected Lie group (Exercise 2.2).

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.1, Corollary 2.11, page 11.

# Verification Notes

- Definition source: Direct from Corollary 2.11
- Confidence rationale: Explicit corollary
- Uncertainties: None
- Cross-reference status: Verified with Exercise 2.8, tables pp. 16-17
