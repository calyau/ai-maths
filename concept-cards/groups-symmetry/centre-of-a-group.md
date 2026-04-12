---
# === CORE IDENTIFICATION ===
concept: Centre of a Group
slug: centre-of-a-group

# === CLASSIFICATION ===
category: conjugacy
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Conjugacy"
chapter_number: 14
pdf_page: 80
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "$Z(G)$"
  - "center of a group"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - conjugacy-class
  - subgroup
extends: []
related:
  - normal-subgroup
  - abelian-group
  - commutator-subgroup
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the centre of a group?"
  - "How does the centre relate to conjugacy classes?"
---

# Quick Definition

The centre of a group $G$, denoted $Z(G)$, is the set of all elements that commute with every element of $G$: $Z(G) = \{x \in G \mid xg = gx \text{ for all } g \in G\}$. It is a subgroup consisting of exactly those elements whose conjugacy class is a singleton.

# Core Definition

The *centre* of a group $G$ consists of all those elements which commute with every element of $G$. It is usually denoted by $Z(G)$ so that $Z(G) = \{x \in G \mid xg = gx, \forall g \in G\}$ (Armstrong, Ch. 14, p. 84).

**(14.1) Theorem.** The centre is a subgroup of $G$ and is made up of the conjugacy classes which contain just one element (Armstrong, p. 84).

# Prerequisites

- **Conjugacy class** — Centre elements are those with singleton conjugacy classes
- **Subgroup** — $Z(G)$ is proved to be a subgroup

# Key Properties

1. $Z(G)$ is a subgroup of $G$ (proved via (5.1))
2. $x \in Z(G)$ iff the conjugacy class of $x$ is $\{x\}$
3. $Z(G) = G$ iff $G$ is abelian
4. $Z(G)$ is always a normal subgroup of $G$ (it is a union of conjugacy classes)
5. $Z(G)$ is always abelian

# Construction / Recognition

## To Compute $Z(G)$:
1. For each $x \in G$, check whether $xg = gx$ for all $g \in G$
2. Equivalently, find the singleton conjugacy classes
3. Collect all such elements; they form $Z(G)$

# Context & Application

Armstrong introduces the centre at the end of Chapter 14 as a subgroup "made up of complete conjugacy classes," foreshadowing the definition of normal subgroups in Chapter 15. The centre measures how far $G$ is from being abelian.

# Examples

**Example 1** (p. 84): The centre of any abelian group is the whole group.

**Example 2** (p. 84): For $n \ge 3$, $Z(S_n) = \{\varepsilon\}$ (trivial centre).

**Example 3** (p. 84): $Z(D_6) = \{e, r^3\}$, from the singleton conjugacy classes $\{e\}$ and $\{r^3\}$.

**Example 4** (p. 84): $Z(GL_n(\mathbb{R}))$ consists of all non-zero scalar multiples of the identity matrix.

**Example 5** (Exercise 14.7): $Z(Q) = \{\pm 1\}$.

# Relationships

## Builds Upon
- **Conjugacy class** — Centre consists of singleton classes
- **Subgroup** — $Z(G)$ is proved to be a subgroup

## Enables
- **Normal subgroup** — $Z(G)$ is always normal
- **Quotient group** — $G/Z(G)$ measures non-commutativity

## Related
- **Abelian group** — $G$ is abelian iff $Z(G) = G$
- **Commutator subgroup** — $[G,G]$ measures non-commutativity from the other direction

# Common Errors

- **Error**: Thinking every normal subgroup is the centre
  **Correction**: The centre is always normal, but many normal subgroups are not the centre

# Common Confusions

- **Confusion**: Confusing "commutes with every element" (centre) with "commutes with a specific element" (centraliser)
  **Clarification**: $Z(G)$ requires commuting with ALL elements; the centraliser $C_G(x)$ only requires commuting with a specific $x$

# Source Reference

Chapter 14: Conjugacy, Theorem (14.1), pp. 84-85 (pdf). Examples (vi)-(ix).

# Verification Notes

- Definition source: Direct from p. 84
- Confidence rationale: HIGH — explicitly defined with theorem and multiple examples
- Uncertainties: None
