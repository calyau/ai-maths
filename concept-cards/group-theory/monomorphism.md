---
# === CORE IDENTIFICATION ===
concept: Monomorphism
slug: monomorphism

# === CLASSIFICATION ===
category: homomorphisms
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Basic Definitions and Results"
chapter_number: 1
pdf_page: 16
section: "Homomorphisms"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - injective homomorphism
  - embedding

# === TYPED RELATIONSHIPS ===
prerequisites:
  - homomorphism
  - kernel
extends:
  - homomorphism
related:
  - isomorphism
  - cayley-theorem
contrasts_with:
  - epimorphism

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an injective homomorphism?"
  - "How can I tell if a homomorphism is injective?"
---

# Quick Definition

A monomorphism (injective homomorphism) is a homomorphism $\alpha: G \to G'$ that is one-to-one. Equivalently, $\mathrm{Ker}(\alpha) = \{e\}$.

# Core Definition

A homomorphism $\alpha: G \to G'$ is injective if and only if $\mathrm{Ker}(\alpha) = \{e\}$. This follows because "$\alpha(g) = \alpha(g') \Rightarrow \alpha(g^{-1}g') = e \Rightarrow g^{-1}g' = e \Rightarrow g = g'$." (Milne, p. 20)

# Prerequisites

- **Homomorphism** — A monomorphism is a homomorphism with injectivity
- **Kernel** — Injectivity is equivalent to trivial kernel

# Key Properties

1. $\alpha$ is injective $\iff$ $\mathrm{Ker}(\alpha) = \{e\}$
2. An injective homomorphism embeds $G$ as a subgroup of $G'$
3. Composition of monomorphisms is a monomorphism

# Construction / Recognition

## To Verify Injectivity:
1. Show $\mathrm{Ker}(\alpha) = \{e\}$, or
2. Show $\alpha(a) = \alpha(b) \Rightarrow a = b$

# Context & Application

Injective homomorphisms realize one group as a subgroup of another. Cayley's theorem (1.22) provides a canonical injection $G \hookrightarrow \mathrm{Sym}(G)$.

# Examples

**Example 1** (p. 16): Cayley's theorem gives an injective homomorphism $G \to \mathrm{Sym}(G)$ via $a \mapsto a_L$.

**Example 2** (p. 16): Corollary 1.23: a finite group of order $n$ embeds as a subgroup of $S_n$.

# Relationships

## Builds Upon
- **homomorphism** — a monomorphism is an injective homomorphism
- **kernel** — trivial kernel characterizes monomorphisms

## Enables
- **cayley-theorem** — provides a canonical monomorphism

## Contrasts With
- **epimorphism** — surjective rather than injective

# Common Errors

- **Error**: Checking injectivity element-by-element instead of using the kernel
  **Correction**: It suffices to show $\mathrm{Ker}(\alpha) = \{e\}$

# Common Confusions

- **Confusion**: Thinking an injective homomorphism must be an isomorphism
  **Clarification**: An isomorphism also requires surjectivity

# Source Reference

Chapter 1, pages 16, 20. Cayley's theorem 1.22, Corollary 1.23.

# Verification Notes

- Definition source: Synthesized from kernel characterization (p. 20)
- Confidence: HIGH — standard concept, explicit criterion given
- Cross-reference status: Verified
- Uncertainties: None
