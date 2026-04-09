---
# === CORE IDENTIFICATION ===
concept: G-Map
slug: g-map

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
pdf_page: 57
section: "Definition and examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - G-equivariant map
  - map of G-sets

# === TYPED RELATIONSHIPS ===
prerequisites:
  - g-set
extends: []
related:
  - group-action
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a morphism of G-sets?"
---

# Quick Definition

A $G$-map is a function $\varphi: X \to Y$ between $G$-sets satisfying $\varphi(gx) = g\varphi(x)$ for all $g \in G$, $x \in X$.

# Core Definition

"A map of $G$-sets (alternatively, a $G$-map or a $G$-equivariant map) is a map $\varphi: X \to Y$ such that $\varphi(gx) = g\varphi(x)$, all $g \in G$, $x \in X$. An isomorphism of $G$-sets is a bijective $G$-map; its inverse is then also a $G$-map" (Milne, p. 57).

# Prerequisites

- **G-set** — $G$-maps are morphisms between $G$-sets

# Key Properties

1. $G$-maps preserve the action structure
2. A bijective $G$-map is an isomorphism of $G$-sets
3. The inverse of a bijective $G$-map is automatically a $G$-map
4. Every transitive $G$-set is isomorphic (as a $G$-set) to $G/H$ for some $H$ (Proposition 4.7)

# Context & Application

$G$-maps are the natural morphisms in the category of $G$-sets. They allow comparison of different actions of the same group.

# Relationships

## Builds Upon
- **g-set**

# Source Reference

Chapter 4: Groups Acting on Sets, "Definition and examples", page 57.

# Verification Notes

- Definition source: Direct from p. 57
- Confidence: HIGH — explicit definition
- Uncertainties: None
