---
# === CORE IDENTIFICATION ===
concept: Canonical Homomorphism
slug: canonical-homomorphism

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
pdf_page: 20
section: "Kernels and quotients"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - natural homomorphism
  - natural map
  - projection map
  - quotient map

# === TYPED RELATIONSHIPS ===
prerequisites:
  - quotient-group
  - normal-subgroup
extends:
  - homomorphism
related:
  - universal-property-of-quotients
  - factorization-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the natural homomorphism from G to G/N?"
  - "What is the kernel of the canonical map?"
---

# Quick Definition

The canonical (or natural) homomorphism is the surjective map $\pi: G \to G/N$ defined by $\pi(a) = aN$. Its kernel is $N$.

# Core Definition

"The natural map $a \mapsto [a]: G \to G/N$ is a homomorphism" with kernel $N$. (Milne, Proposition 1.42, p. 20)

# Prerequisites

- **Quotient group** — the canonical map targets $G/N$
- **Normal subgroup** — $N$ must be normal for $G/N$ to exist

# Key Properties

1. $\pi$ is surjective (every coset $aN$ is in the image)
2. $\mathrm{Ker}(\pi) = N$
3. $\pi$ satisfies a universal property (Proposition 1.43)

# Context & Application

The canonical homomorphism is the prototype of all surjective homomorphisms. The universal property states that any homomorphism $\alpha: G \to G'$ with $\alpha(N) = \{e\}$ factors uniquely through $\pi$.

# Examples

**Example 1** (p. 21): The map $n \mapsto [n]: \mathbb{Z} \to \mathbb{Z}/m\mathbb{Z}$ is the canonical homomorphism with kernel $m\mathbb{Z}$.

# Relationships

## Builds Upon
- **quotient-group** — the target of the canonical map

## Enables
- **universal-property-of-quotients** — the canonical map has a universal property
- **factorization-theorem** — every homomorphism factors through a canonical map

# Source Reference

Chapter 1, Proposition 1.42, page 20.

# Verification Notes

- Definition source: From Proposition 1.42
- Confidence: HIGH — explicit construction
- Uncertainties: None
