---
# === CORE IDENTIFICATION ===
concept: Injective Function
slug: injective-function

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
  - one-to-one function
  - injection
  - one-to-one

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mapping
extends:
  - mapping
related:
  - surjective-function
  - bijective-function
contrasts_with:
  - surjective-function

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

A map $f: A \to B$ is injective (one-to-one) if distinct elements of $A$ map to distinct elements of $B$; that is, $a_1 \neq a_2$ implies $f(a_1) \neq f(a_2)$.

# Core Definition

"A map is one-to-one or injective if $a_1 \neq a_2$ implies $f(a_1) \neq f(a_2)$. Equivalently, a function is one-to-one if $f(a_1) = f(a_2)$ implies $a_1 = a_2$" (Judson, p. 20).

# Prerequisites

- **Mapping** — Injectivity is a property of mappings

# Key Properties

1. $f(a_1) = f(a_2) \Rightarrow a_1 = a_2$ (contrapositive characterization)
2. The composition of two injective maps is injective (Theorem 1.15)
3. An injective map need not be surjective

# Construction / Recognition

## To Prove Injectivity:
1. Assume $f(a_1) = f(a_2)$
2. Show that $a_1 = a_2$

## To Disprove Injectivity:
1. Find two distinct elements $a_1 \neq a_2$ with $f(a_1) = f(a_2)$

# Context & Application

Injectivity is one of two key properties (along with surjectivity) required for a bijection. Bijective maps are invertible, which is essential for group isomorphisms.

# Examples

**Example 1** (p. 20): $f: \mathbb{Z} \to \mathbb{Q}$ defined by $f(n) = n/1$ is one-to-one but not onto.

# Relationships

## Builds Upon
- **mapping** — Injectivity is a property of mappings

## Enables
- **bijective-function** — Bijection = injection + surjection
- **inverse-mapping** — Bijective maps have inverses

## Contrasts With
- **surjective-function** — Injectivity and surjectivity are independent properties

# Common Errors

- **Error**: Proving injectivity by showing $a_1 = a_2$ implies $f(a_1) = f(a_2)$
  **Correction**: That is just the definition of a function; injectivity requires the converse: $f(a_1) = f(a_2)$ implies $a_1 = a_2$

# Common Confusions

- **Confusion**: Thinking injective means surjective
  **Clarification**: A function can be injective without being surjective, and vice versa

# Source Reference

Chapter 1: Preliminaries, Section 1.2, page 20.

# Verification Notes

- Definition source: Direct quote from p. 20
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
