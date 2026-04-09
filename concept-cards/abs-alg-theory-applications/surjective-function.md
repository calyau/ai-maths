---
# === CORE IDENTIFICATION ===
concept: Surjective Function
slug: surjective-function

# === CLASSIFICATION ===
category: foundations
subcategory: set-theory
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Preliminaries"
chapter_number: 1
pdf_page: 20
section: "Cartesian Products and Mappings"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - onto function
  - surjection
  - onto

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mapping
extends:
  - mapping
related:
  - injective-function
  - bijective-function
contrasts_with:
  - injective-function

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

A map $f: A \to B$ is surjective (onto) if every element of $B$ is the image of some element in $A$; that is, $f(A) = B$.

# Core Definition

"If $f: A \to B$ is a map and the image of $f$ is $B$, i.e., $f(A) = B$, then $f$ is said to be onto or surjective. In other words, if there exists an $a \in A$ for each $b \in B$ such that $f(a) = b$, then $f$ is onto" (Judson, p. 20).

# Prerequisites

- **Mapping** — Surjectivity is a property of mappings

# Key Properties

1. For every $b \in B$, there exists $a \in A$ such that $f(a) = b$
2. The composition of two surjective maps is surjective (Theorem 1.15)
3. A surjective map need not be injective

# Construction / Recognition

## To Prove Surjectivity:
1. Let $b$ be an arbitrary element of $B$
2. Find (or construct) an element $a \in A$ such that $f(a) = b$

## To Disprove Surjectivity:
1. Find an element $b \in B$ that is not in the image $f(A)$

# Context & Application

Surjectivity ensures every element in the codomain is "reachable." Together with injectivity, it gives bijectivity, which is required for invertibility and group isomorphisms.

# Examples

**Example 1** (p. 20): $g: \mathbb{Q} \to \mathbb{Z}$ defined by $g(p/q) = p$ (where $p/q$ is in lowest terms with positive denominator) is onto but not one-to-one.

# Relationships

## Builds Upon
- **mapping** — Surjectivity is a property of mappings

## Enables
- **bijective-function** — Bijection = injection + surjection

## Contrasts With
- **injective-function** — Independent property

# Common Errors

- **Error**: Claiming surjectivity without showing every element of $B$ has a preimage
  **Correction**: Must demonstrate for arbitrary $b \in B$ that some $a \in A$ maps to it

# Common Confusions

- **Confusion**: Confusing the codomain with the range
  **Clarification**: A function is surjective when its range equals its codomain; if $f: A \to B$ but $f(A) \subsetneq B$, then $f$ is not surjective

# Source Reference

Chapter 1: Preliminaries, Section 1.2, page 20.

# Verification Notes

- Definition source: Direct quote from p. 20
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
