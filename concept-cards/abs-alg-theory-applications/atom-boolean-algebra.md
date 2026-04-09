---
# === CORE IDENTIFICATION ===
concept: Atom of a Boolean Algebra
slug: atom-boolean-algebra

# === CLASSIFICATION ===
category: lattice-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Lattices and Boolean Algebras"
chapter_number: 19
pdf_page: 258
section: "19.2 Boolean Algebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - boolean-algebra
extends: []
related:
  - finite-boolean-algebra-classification
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an atom in a Boolean algebra?"
  - "How are finite Boolean algebras classified?"
---

# Quick Definition

An atom of a finite Boolean algebra $B$ is a nonzero element $a$ such that for any $b \in B$ with $b \neq O$, $a \wedge b = a$ implies $b = a$. Equivalently, $a$ is minimal among nonzero elements.

# Core Definition

"An element $a \in B$ is an atom of $B$ if $a \neq O$ and $a \wedge b = a$ for all $b \in B$ with $b \neq O$. Equivalently, $a$ is an atom of $B$ if there is no $b \in B$ with $b \neq O$ distinct from $a$ such that $O \preceq b \preceq a$" (Judson, p. 258).

# Prerequisites

- **Boolean algebra** — Atoms are defined in Boolean algebras

# Key Properties

1. An atom is a minimal nonzero element
2. Every nonzero element $b$ has some atom $a \preceq b$ (Lemma 19.18)
3. Distinct atoms have meet $O$: $a \wedge b = O$ for atoms $a \neq b$ (Lemma 19.19)
4. Every element is a join of atoms (Lemma 19.22)
5. The representation as a join of atoms is unique

# Construction / Recognition

## To Identify:
1. Find elements $a$ with $a \neq O$
2. Check that no element $b$ satisfies $O \prec b \prec a$

# Context & Application

Atoms are the "building blocks" of finite Boolean algebras. They correspond to singleton sets in the power set representation. The number of atoms determines the size of the Boolean algebra ($2^n$ elements for $n$ atoms).

# Examples

**Example 1**: In $\mathcal{P}(\{a,b,c\})$, the atoms are $\{a\}, \{b\}, \{c\}$ (the singleton sets).

**Example 2**: Every element can be written as a union of singletons: $\{a,c\} = \{a\} \cup \{c\}$.

# Relationships

## Enables
- **Finite Boolean algebra classification** — Every finite Boolean algebra is isomorphic to $\mathcal{P}(X)$ where $X$ is the set of atoms

# Common Errors

- **Error**: Assuming $O$ is an atom
  **Correction**: By definition, atoms are nonzero

# Common Confusions

- **Confusion**: Thinking atoms can be decomposed further
  **Clarification**: Atoms are exactly the elements that cannot be decomposed (minimal nonzero elements)

# Source Reference

Chapter 19: Lattices and Boolean Algebras, Section 19.2, pages 258-260. See Lemmas 19.18-19.22.

# Verification Notes

- Definition source: Direct from p. 258
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
