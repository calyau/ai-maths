---
# === CORE IDENTIFICATION ===
concept: Inner Form
slug: inner-form

# === CLASSIFICATION ===
category: galois-cohomology
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Reductive Groups: General Case"
chapter_number: 6
pdf_page: 393
section: "Reductive algebraic groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - inner twist

# === TYPED RELATIONSHIPS ===
prerequisites:
  - form-of-algebraic-group
  - galois-cohomology-of-algebraic-groups
  - reductive-algebraic-group
extends:
  - form-of-algebraic-group
related:
  - tits-index
  - anisotropic-kernel
contrasts_with:
  - outer-form

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Galois cohomology classify forms of algebraic groups?"
---

# Quick Definition

An inner form of a split simply connected group $G_0$ of type $X_v$ is a form $G$ whose cohomology class lies in the image of $H^1(k, G^{\mathrm{ad}})$ in $H^1(k, \mathrm{Aut}(G_{0,k^{\mathrm{al}}}))$. Inner forms are twisted only by inner automorphisms.

# Core Definition

"Let $G_0$ be the split simply connected group of type $X_v$, and let $G$ be a form of $G_0$. Let $c$ be its cohomology class. If $c \in H^1(k, G^{\mathrm{ad}})$, then $G$ is called an *inner form* of $G_0$." (Remark 1.22, Milne, p. 393)

In general, $c$ maps to an element of $H^1(k, \mathrm{Sym}(D)) = \mathrm{Hom}_{\mathrm{continuous}}(\Gamma, \mathrm{Sym}(D))$ where $D$ is the Dynkin diagram. If $\Delta$ is the kernel of this homomorphism and $L = (k^{\mathrm{al}})^\Delta$, with $z = (\Gamma : \Delta)$, then $G$ is said to be of type ${}^z X_v$.

# Prerequisites

- **Form of algebraic group** — inner forms are a special class of forms
- **Galois cohomology of algebraic groups** — the classification uses $H^1(k, G^{\mathrm{ad}})$
- **Reductive algebraic group** — inner forms are defined for reductive groups via their Dynkin diagrams

# Key Properties

1. Inner forms correspond to cocycles valued in $G^{\mathrm{ad}}(k^{\mathrm{al}})$, i.e., inner automorphisms
2. The centre $Z(G)$ of an inner form has the same points as $Z(G_0)$ but possibly different Galois action
3. For an inner form, $\Gamma$ acts on the Dynkin diagram through the standard action (the image in $\mathrm{Sym}(D)$ is trivial), so $z = 1$ and the type is ${}^1 X_v$
4. Outer forms have $z > 1$; the possible values of $z$ are constrained by $|\mathrm{Sym}(D)|$

# Construction / Recognition

## To Recognize:
1. Compute the cohomology class $c$ of $G$ in $H^1(k, \mathrm{Aut}(G_{0,k^{\mathrm{al}}}))$
2. Check whether $c$ lies in the image of $H^1(k, G^{\mathrm{ad}}) \to H^1(k, \mathrm{Aut}(G_{0,k^{\mathrm{al}}}))$
3. If yes, $G$ is an inner form; if no, it is an outer form of type ${}^z X_v$

# Context & Application

The distinction between inner and outer forms is fundamental to the classification of semisimple groups over arbitrary fields. Inner forms preserve the Dynkin diagram symmetry, while outer forms involve a nontrivial action of $\Gamma$ on the diagram. For $A_n$ ($n \geq 2$), $D_n$, and $E_6$, which have nontrivial diagram automorphisms, outer forms exist and give rise to unitary groups, quasi-split forms, etc.

# Examples

**Example 1** (p. 393): For type $A_n$, the Dynkin diagram has a symmetry of order 2 (for $n \geq 2$). The split group is $\mathrm{SL}_{n+1}$. Inner forms correspond to groups $\mathrm{SL}_m(D)$ where $D$ is a division algebra over $k$. Outer forms (type ${}^2 A_n$) include the unitary groups.

**Example 2** (p. 393): The symmetry group of $D_4$ is $S_3$, so there are forms of types ${}^1 D_4$, ${}^2 D_4$, ${}^3 D_4$, and ${}^6 D_4$ (triality forms).

# Relationships

## Builds Upon
- **Form of algebraic group** — an inner form is a specific type of form

## Enables
- **Tits index** — the index records whether a form is inner or outer
- **Anisotropic kernel** — the anisotropic kernel description depends on the form type

## Contrasts With
- **Outer form** — outer forms involve nontrivial Dynkin diagram automorphisms

# Common Errors

- **Error**: Assuming all forms of a group are inner
  **Correction**: Groups with nontrivial Dynkin diagram symmetries ($A_n$, $D_n$, $E_6$) admit outer forms

# Common Confusions

- **Confusion**: Thinking "inner form" means "isomorphic"
  **Clarification**: Inner forms are genuinely different algebraic groups over $k$ (e.g., $\mathrm{SL}_2(D)$ for a division quaternion algebra $D$ is an inner form of $\mathrm{SL}_4$)

# Source Reference

Chapter VI: The Structure of Reductive Groups: General Case, Section 1d, Remark 1.22, page 393.

# Verification Notes

- Definition source: Direct quote from Remark 1.22
- Confidence: HIGH — explicit definition
- Uncertainties: None
- Cross-reference status: Verified
