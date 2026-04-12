---
# === CORE IDENTIFICATION ===
concept: Conjugacy Class
slug: conjugacy-class

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - conjugacy-equivalence-relation
  - group
extends:
  - equivalence-class
related:
  - conjugation-by-g
  - centre-of-a-group
  - normal-subgroup
  - cycle-structure-conjugacy
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do conjugacy classes partition a group?"
  - "What is a conjugacy class?"
---

# Quick Definition

The conjugacy class of an element $x$ in a group $G$ is the set of all elements of the form $gxg^{-1}$ for $g \in G$. The distinct conjugacy classes partition $G$.

# Core Definition

The relation of conjugacy was introduced in Chapter 12 and shown to be an equivalence relation. The equivalence classes are called *conjugacy classes* (Armstrong, Ch. 14, p. 80). Elements in the same conjugacy class have the same order, since conjugation by $g$ is an isomorphism that preserves element orders.

# Prerequisites

- **Conjugacy as equivalence relation** — Conjugacy classes are the equivalence classes of conjugacy
- **Group** — The group operation defines conjugation

# Key Properties

1. Conjugacy classes partition $G$ (by Theorem 12.2)
2. Elements in the same class have the same order
3. In an abelian group, every conjugacy class is a singleton $\{x\}$
4. The identity always forms a singleton class $\{e\}$
5. Singleton classes $\{x\}$ correspond to elements of the centre $Z(G)$

# Construction / Recognition

## To Compute Conjugacy Classes:
1. For each $x \in G$, compute $gxg^{-1}$ for all $g \in G$
2. Collect the resulting elements into the class of $x$
3. Group elements into classes; verify they partition $G$

# Context & Application

Conjugacy classes are central to the structure theory of groups. Armstrong works out conjugacy classes for several important groups ($D_6$, $S_n$, $A_4$, $O_2$) in Chapter 14, then uses them in Chapter 15 to define normal subgroups as unions of conjugacy classes.

# Examples

**Example 1** (p. 80): In $D_6$, the conjugacy classes are:
$\{e\}$, $\{r, r^5\}$, $\{r^2, r^4\}$, $\{r^3\}$, $\{s, r^2 s, r^4 s\}$, $\{rs, r^3 s, r^5 s\}$.

**Example 2** (p. 80): In an abelian group, conjugacy classes are singletons: $gxg^{-1} = x$ for all $g$.

**Example 3** (p. 82): In $A_4$, the conjugacy classes are $\{\varepsilon\}$, $\{(12)(34), (13)(24), (14)(23)\}$, $\{(123), (124), (134), (234)\}$, $\{(132), (142), (143), (243)\}$.

# Relationships

## Builds Upon
- **Equivalence class** — Conjugacy classes are a specific type of equivalence class

## Enables
- **Normal subgroup** — Defined as a union of conjugacy classes
- **Centre of a group** — Elements whose conjugacy class is a singleton
- **Class equation** — Relates $|G|$ to conjugacy class sizes (developed in later chapters)

## Related
- **Conjugation by $g$** — The map producing conjugates
- **Cycle structure conjugacy** — In $S_n$, conjugacy = same cycle structure

# Common Errors

- **Error**: Forgetting that the identity forms its own conjugacy class
  **Correction**: $geg^{-1} = e$ for all $g$, so $\{e\}$ is always a conjugacy class

# Common Confusions

- **Confusion**: Thinking that elements of the same order are conjugate
  **Clarification**: Same order is necessary but not sufficient. In $A_4$, the 3-cycles $(123)$ and $(132)$ have the same order but are in different conjugacy classes.

# Source Reference

Chapter 14: Conjugacy, pp. 80-85 (pdf). Examples (i)-(v).

# Verification Notes

- Definition source: Direct from p. 80, recalling Ch. 12
- Confidence rationale: HIGH — central concept with extensive worked examples
- Uncertainties: None
