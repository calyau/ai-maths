---
# === CORE IDENTIFICATION ===
concept: Semilinear Action
slug: semilinear-action

# === CLASSIFICATION ===
category: galois-cohomology
subcategory: descent
tier: advanced

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Reductive Groups: General Case"
chapter_number: 6
pdf_page: 385
section: "Classifying bilinear forms"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - semi-linear action

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-action
extends: []
related:
  - form-of-algebraic-group
  - noncommutative-galois-cohomology
  - galois-descent
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before understanding Galois cohomology of algebraic groups?"
---

# Quick Definition

A semilinear action of a Galois group $\Gamma$ on a $K$-vector space $V$ is an action by $k$-linear maps satisfying $\sigma(cv) = \sigma c \cdot \sigma v$ for all $\sigma \in \Gamma$, $c \in K$, $v \in V$. It is the key ingredient in Galois descent.

# Core Definition

Let $K$ be a finite Galois extension of $k$ with Galois group $\Gamma$. Let $V$ be a finite-dimensional $K$-vector space. "A **semi-linear action** of $\Gamma$ on $V$ is a homomorphism $\Gamma \to \mathrm{Aut}_{k\text{-lin}}(V)$ such that $\sigma(cv) = \sigma c \cdot \sigma v$ all $\sigma \in \Gamma$, $c \in K$, $v \in V$." (Milne, p. 385)

The key descent result (Proposition 1.2): the functor $V \mapsto K \otimes_k V$ from $k$-vector spaces to $K$-vector spaces endowed with a semilinear $\Gamma$-action is an equivalence of categories, with quasi-inverse $V \mapsto V^\Gamma$.

# Prerequisites

- **Group action** — a semilinear action is a special type of group action

# Key Properties

1. The action is $k$-linear but not $K$-linear (it twists scalars)
2. For $V = K \otimes_k V_0$, the canonical semilinear action is $\sigma(c \otimes v) = \sigma c \otimes v$
3. The fixed space $V^\Gamma$ is a $k$-vector space with $K \otimes_k V^\Gamma \simeq V$ (Proposition 1.2)
4. Twisting the semilinear action by a 1-cocycle gives a new semilinear action and hence a new descent

# Construction / Recognition

## To Construct:
1. Start with a $k$-vector space $V_0$
2. Form $V = K \otimes_k V_0$
3. Define $\sigma(c \otimes v) = \sigma c \otimes v$

## To Twist by a Cocycle:
1. Given a 1-cocycle $(a_\sigma)$ in $\mathrm{GL}(V)$
2. Define ${}^\sigma x = a_\sigma \cdot \sigma x$
3. This new semilinear action descends to a different $k$-form $V_1 = \{x \in V \mid {}^\sigma x = x\}$

# Context & Application

Semilinear actions underlie all of Galois descent theory. The proof that $H^1(\Gamma, \mathrm{GL}_n(K)) = 1$ ultimately reduces to the equivalence of categories given by Proposition 1.2. The technique of twisting a semilinear action by a cocycle is how one constructs forms from cohomology classes.

# Examples

**Example 1** (p. 385): For $V_0 = k^n$, the canonical semilinear action on $K^n = K \otimes_k k^n$ is $\sigma(c_1, \ldots, c_n) = (\sigma c_1, \ldots, \sigma c_n)$, and $(K^n)^\Gamma = k^n$.

**Example 2** (pp. 386-387): Given a bilinear form $(V_0, \phi_0)$ and a 1-cocycle $(a_\sigma)$ in $\mathcal{A}(K)$, the twisted semilinear action ${}^\sigma x = a_\sigma \cdot \sigma x$ produces a new $k$-vector space $V_1 = \{x \in V_K \mid {}^\sigma x = x\}$ with a descended bilinear form.

# Relationships

## Builds Upon
- **Group action** — semilinear actions extend the concept of group actions

## Enables
- **Form of algebraic group** — twisting semilinear actions produces forms
- **Noncommutative Galois cohomology** — the descent equivalence proves vanishing results

# Common Errors

- **Error**: Treating a semilinear action as $K$-linear
  **Correction**: $\sigma(cv) = \sigma c \cdot \sigma v \neq c \cdot \sigma v$ in general; the action twists scalars

# Common Confusions

- **Confusion**: Thinking the fixed space $V^\Gamma$ is a $K$-subspace
  **Clarification**: $V^\Gamma$ is a $k$-subspace, not a $K$-subspace, since $\sigma$ acts nontrivially on $K$

# Source Reference

Chapter VI: The Structure of Reductive Groups: General Case, Section 1b, pages 385-386. Proposition 1.2.

# Verification Notes

- Definition source: Direct quote from p. 385
- Confidence: HIGH — explicit definition with clear notation
- Uncertainties: None
- Cross-reference status: Verified
