---
# === CORE IDENTIFICATION ===
concept: Group Action
slug: group-action

# === CLASSIFICATION ===
category: group-actions
subcategory: definitions
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Groups Acting on Sets"
chapter_number: 4
pdf_page: 56
section: "Definition and examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - left action

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - homomorphism
extends: []
related:
  - g-set
  - faithful-action
  - orbit
  - stabilizer
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group action?"
---

# Quick Definition

A left action of a group $G$ on a set $X$ is a map $G \times X \to X$, $(g, x) \mapsto gx$, satisfying $1x = x$ and $(g_1 g_2)x = g_1(g_2 x)$.

# Core Definition

"Let $X$ be a set and let $G$ be a group. A left action of $G$ on $X$ is a mapping $(g, x) \mapsto gx : G \times X \to X$ such that (a) $1x = x$ for all $x \in X$; (b) $(g_1 g_2)x = g_1(g_2 x)$, all $g_1, g_2 \in G$, $x \in X$" (Milne, Definition 4.1, p. 56).

# Prerequisites

- **Group** — The group $G$ that acts
- **Homomorphism** — An action is equivalent to a homomorphism $G \to \operatorname{Sym}(X)$

# Key Properties

1. An action is equivalent to a homomorphism $g \mapsto g_L : G \to \operatorname{Sym}(X)$ (equation (18))
2. Each $g \in G$ acts as a bijection $X \to X$ with inverse $g^{-1}$
3. An action is trivial if $gx = x$ for all $g \in G$, $x \in X$
4. A right action $X \times G \to X$ can be turned into a left action by $g * x = xg^{-1}$

# Construction / Recognition

## To define a group action:
1. Specify the group $G$ and set $X$
2. Define $gx$ for all $g \in G$, $x \in X$
3. Verify: $1x = x$ for all $x$
4. Verify: $(g_1 g_2)x = g_1(g_2 x)$ for all $g_1, g_2, x$

# Context & Application

Group actions are one of the most powerful tools in group theory. They unify conjugation, coset spaces, permutation representations, and geometric symmetries into a single framework.

# Examples

**Example 1** (p. 56): Every subgroup of $\operatorname{Sym}(X)$ acts faithfully on $X$.

**Example 2** (p. 56): Any subgroup $H \leq G$ acts on $G$ by left translation: $(h, x) \mapsto hx$.

**Example 3** (p. 56): $G$ acts on $G/H$ by left multiplication: $(g, C) \mapsto gC$.

**Example 4** (p. 56): $G$ acts on itself by conjugation: $(g, x) \mapsto gxg^{-1}$.

# Relationships

## Enables
- **g-set** — A set with a $G$-action
- **orbit** — Equivalence classes under the action
- **stabilizer** — Subgroup fixing a point
- **faithful-action** — Action with trivial kernel

# Common Errors

- **Error**: Confusing left and right actions
  **Correction**: For a left action $(g_1 g_2)x = g_1(g_2 x)$; for a right action $x(g_1 g_2) = (xg_1)g_2$. Converting: $g * x = xg^{-1}$

# Source Reference

Chapter 4: Groups Acting on Sets, "Definition and examples", Definition 4.1, page 56.

# Verification Notes

- Definition source: Direct quote from Definition 4.1, p. 56
- Confidence: HIGH — explicit definition
- Uncertainties: None
