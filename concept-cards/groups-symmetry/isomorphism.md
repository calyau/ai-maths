---
# === CORE IDENTIFICATION ===
concept: Isomorphism
slug: isomorphism

# === CLASSIFICATION ===
category: fundamentals
subcategory: maps
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Isomorphisms"
chapter_number: 7
pdf_page: 39
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "group isomorphism"

# === TYPED RELATIONSHIPS ===
prerequisites: []
related:
  - isomorphic-groups
  - isomorphism-preserves-identity
  - isomorphism-preserves-inverses
  - isomorphism-preserves-order
  - isomorphism-preserves-subgroups
  - isomorphism-preserves-commutativity
  - cayleys-theorem
contrasts_with: []
extends: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an isomorphism between groups?"
  - "How is an isomorphism defined?"
---

# Quick Definition

An isomorphism between groups $G$ and $G'$ is a bijection $\varphi: G \to G'$ that preserves the group operation: $\varphi(xy) = \varphi(x)\varphi(y)$ for all $x, y \in G$.

# Core Definition

"Two groups $G$ and $G'$ are **isomorphic** if there is a bijection $\varphi$ from $G$ to $G'$ which satisfies $\varphi(xy) = \varphi(x)\varphi(y)$ for all $x, y \in G$. The function $\varphi$ is called an **isomorphism** between $G$ and $G'$" (Armstrong, p. 40).

The definition requires two conditions: (1) $\varphi$ is a bijection between $G$ and $G'$, ensuring they have the same size, and (2) $\varphi$ respects multiplication, so "it does not matter whether we first combine two elements in $G$ and then send their product into $G'$ using $\varphi$, or first send the elements separately into $G'$ via $\varphi$ and then combine their images in $G'$" (p. 40).

# Prerequisites

This is a foundational concept for the study of group structure.

# Key Properties

1. A bijection $\varphi: G \to G'$ with $\varphi(xy) = \varphi(x)\varphi(y)$
2. The inverse $\varphi^{-1}: G' \to G$ is also an isomorphism (p. 40)
3. The composition of two isomorphisms is an isomorphism (p. 42)
4. Isomorphism is symmetric: if $G \cong G'$ then $G' \cong G$
5. Isomorphism is an equivalence relation on groups

# Construction / Recognition

## To Construct an Isomorphism:
1. Define a function $\varphi: G \to G'$
2. Verify $\varphi$ is injective (if $\varphi(x) = \varphi(y)$ then $x = y$)
3. Verify $\varphi$ is surjective (every element of $G'$ is in the range)
4. Verify the homomorphism property: $\varphi(xy) = \varphi(x)\varphi(y)$ for all $x, y$

## To Show Groups Are Not Isomorphic:
1. Find a group-theoretic property that differs (order, abelianness, element orders, number of subgroups, etc.)

# Context & Application

Isomorphism is the central notion of "sameness" in group theory. Two isomorphic groups are algebraically indistinguishable; they differ only in how their elements are labelled. Armstrong writes: "Therefore, $G'$ is really just $G$ in disguise" (p. 40). The notation $G \cong G'$ indicates isomorphism.

# Examples

**Example** (p. 39-40): The group of plane symmetries of a chessboard $\{e, r, q_1, q_2\}$ is isomorphic to $\{1, 3, 5, 7\}$ under multiplication modulo 8, via $e \to 1$, $r \to 3$, $q_1 \to 5$, $q_2 \to 7$.

**Example** (p. 40): $\varphi: \mathbb{R} \to \mathbb{R}^{pos}$ defined by $\varphi(x) = e^x$ is an isomorphism (addition to multiplication).

**Example** (p. 41): Any infinite cyclic group is isomorphic to $\mathbb{Z}$ via $\varphi(x^m) = m$.

**Example** (p. 41): Any finite cyclic group of order $n$ is isomorphic to $\mathbb{Z}_n$.

**Example** (p. 41): $\mathbb{Q}$ is not isomorphic to $\mathbb{Q}^{pos}$ because $\varphi(x/2)$ would need to be $\sqrt{2} \notin \mathbb{Q}$.

# Relationships

## Enables
- **Isomorphic groups** — The relation between groups connected by an isomorphism
- **Cayley's theorem** — Every group is isomorphic to a permutation group

## Related
- **Isomorphism preserves identity** — $\varphi(e_G) = e_{G'}$
- **Isomorphism preserves inverses** — $\varphi(x^{-1}) = \varphi(x)^{-1}$
- **Isomorphism preserves order** — Order of $\varphi(x)$ equals order of $x$
- **Isomorphism preserves subgroups** — $\varphi(H)$ is a subgroup when $H$ is
- **Isomorphism preserves commutativity** — If $G$ is abelian, so is $G'$

# Common Errors

- **Error**: Checking only the homomorphism property without verifying bijectivity.
  **Correction**: An isomorphism must be a bijection. A function satisfying $\varphi(xy) = \varphi(x)\varphi(y)$ that is not bijective is a homomorphism, not an isomorphism.

# Common Confusions

- **Confusion**: Thinking there is only one isomorphism between isomorphic groups.
  **Clarification**: There can be many distinct isomorphisms. For example, there are two isomorphisms from $\{1, i, -1, -i\}$ to $\mathbb{Z}_4$ (p. 41).

# Source Reference

Chapter 7: Isomorphisms, pages 39-43 (pdf pp. 39-43). Definition on p. 40; properties on pp. 41-42; examples throughout.

# Verification Notes

- Definition: Direct quote from p. 40
- Properties: All proved on pp. 41-42
- Examples: Directly from source
- Confidence: HIGH — explicit definition with extensive treatment
