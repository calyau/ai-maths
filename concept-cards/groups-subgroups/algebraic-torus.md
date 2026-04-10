---
concept: Algebraic Torus
slug: algebraic-torus
category: multiplicative-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 170
section: "14e Groups of multiplicative type"
extraction_confidence: high
aliases:
  - torus
  - k-torus
prerequisites:
  - group-of-multiplicative-type
  - split-torus
extends:
  - group-of-multiplicative-type
related:
  - character-module
  - cocharacter
  - anisotropic-torus
contrasts_with:
  - unipotent-group
answers_questions:
  - "What is an algebraic torus?"
  - "How do characters and cocharacters pair in the theory of tori?"
---

# Quick Definition

A torus is an algebraic group T such that T_{k^sep} is a split torus (a product of copies of G_m). Equivalently, it is a group of multiplicative type with X*(T) torsion-free. The rank of T is the rank of the free abelian group X*(T).

# Core Definition

A *torus* is an algebraic group T such that T_{k^sep} is a split torus (Definition 14.24). Equivalently, T is of multiplicative type and X*(T) is torsion-free. Every torus T has unique subtori T_s (largest split subtorus) and T_a (largest anisotropic subtorus) with T_s . T_a = T and T_s cap T_a finite (Corollary 14.26). A torus is *anisotropic* if X(T) = 0, i.e., X*(T)^Gamma = 0 (Milne, pp. 170-171).

# Prerequisites

- **Group of multiplicative type** -- Tori are the torsion-free case
- **Split torus** -- The split form of a torus

# Key Properties

1. T is a torus iff T_{k^sep} = G_m^n for some n (the rank)
2. X*(T) is a free abelian group of rank n with continuous Gamma-action
3. T = T_s . T_a where T_s is split and T_a is anisotropic (Corollary 14.26)
4. The simple factors correspond to simple Gamma-modules in X*(T)_Q (Proposition 14.25)
5. Connected actions on tori are trivial (rigidity, Theorem 14.32)
6. Torsion points are dense: if alpha|_{T_n} = id for all n, then alpha = id (Proposition 14.35)

# Construction / Recognition

## To Construct:
1. Choose a free abelian group M of finite rank with continuous Gamma-action
2. The torus T with X*(T) = M is the unique group of multiplicative type with this character module

## To Recognize:
1. Check that G is of multiplicative type (commutative, Hom(G, G_a) = 0)
2. Check that X*(G) is torsion-free (equivalently, G is connected and smooth)

# Context & Application

Tori play a central role in the structure theory of reductive groups. Every reductive group contains a maximal torus, and the root system is defined relative to the adjoint action of a maximal torus. The character lattice X*(T) encodes the representation theory.

# Examples

**Example 1** (p. 170): The standard split torus G_m^n has X*(T) = Z^n with trivial Gamma-action.

**Example 2** (p. 170): Over R with X*(T) = Z and the nontrivial Gamma-action m -> -m, the torus T(R) = {z in C^x | |z| = 1} is anisotropic (has no R-rational characters).

**Example 3** (p. 170): For K/k finite separable, the Weil restriction (G_m)_{K/k} is a torus of rank [K:k] with X*(T) = Z^{Hom_k(K, k^sep)}.

# Relationships

## Builds Upon
- **Group of multiplicative type** -- Tori are the connected smooth case
- **Split torus** -- The simplest case: G_m^n

## Enables
- **Solvable algebraic group** -- Tori appear in the structure (T_n -> G -> G/G_u)
- **Root system** -- Defined via maximal torus in a reductive group

## Contrasts With
- **Unipotent group** -- Hom(unipotent, torus) = 0

# Common Confusions

- **Confusion**: Thinking all tori are split (isomorphic to G_m^n over k)
  **Clarification**: A torus T is split only if the Gamma-action on X*(T) is trivial. Non-split tori are common and important (e.g., anisotropic tori over R).

# Source Reference

Chapter I: Basic Theory of Affine Groups, Sections 14e and 14.16, pages 168-171. Definition 14.24, Propositions 14.25-14.26.

# Verification Notes

- Definition source: Direct from Definition 14.24
- Confidence rationale: Explicit definition with structural decomposition results
- Uncertainties: None
- Cross-reference status: Verified
