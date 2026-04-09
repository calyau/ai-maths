---
# === CORE IDENTIFICATION ===
concept: Central Extension
slug: central-extension

# === CLASSIFICATION ===
category: automorphisms-extensions
subcategory: extensions
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Automorphisms and Extensions"
chapter_number: 3
pdf_page: 49
section: "Extensions of groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - extension-of-groups
  - centre-of-group
extends:
  - extension-of-groups
related:
  - split-extension
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a central extension?"
---

# Quick Definition

A central extension is an extension $1 \to N \xrightarrow{\iota} G \xrightarrow{\pi} Q \to 1$ where $\iota(N) \subset Z(G)$.

# Core Definition

"An extension is central if $\iota(N) \subset Z(G)$" (Milne, p. 49). A semidirect product $N \rtimes_\theta Q$ gives a central extension if and only if $\theta$ is trivial and $N$ is commutative.

# Prerequisites

- **Extension of groups** — A central extension is a special kind of extension
- **Centre of group** — The image of $N$ must lie in the centre

# Key Properties

1. $\iota(N) \subset Z(G)$, so $N$ acts trivially on $G$ by conjugation
2. A semidirect product extension is central iff $\theta$ is trivial and $N$ is abelian
3. The quaternion group gives a central extension $1 \to C_2 \to Q_8 \to C_2 \times C_2 \to 1$ that does not split

# Examples

**Example 1** (p. 50): $1 \to Z(Q) \to Q \to Q/Z(Q) \to 1$ for the quaternion group is a central extension that does not split.

# Relationships

## Builds Upon
- **extension-of-groups** — Central extension adds the condition $\iota(N) \subset Z(G)$

# Source Reference

Chapter 3: Automorphisms and Extensions, "Extensions of groups", page 49.

# Verification Notes

- Definition source: Direct from p. 49
- Confidence: HIGH — explicit definition
- Uncertainties: None
