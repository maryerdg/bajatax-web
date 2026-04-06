# Design System: High-End Editorial for Baja Tax
 
## 1. Overview & Creative North Star
### Creative North Star: "The Architectural Ledger"
This design system moves beyond the generic "corporate blue" aesthetic to create a digital presence that feels as solid and prestigious as a heritage accounting firm. The "Architectural Ledger" concept treats the screen as a series of physical planes—high-quality paper, heavy vellum, and frosted glass—stacked with mathematical precision.
 
We break the standard grid-template look by using **intentional asymmetry** and **normal (2) white space**. Layouts should feel like a premium finance journal: large, bold headlines paired with hyper-clean data visualizations. By leaning into tonal depth rather than lines, we create a sense of effortless authority and modern trust.
 
---
 
## 2. Colors
Our palette is rooted in deep, authoritative navies and crisp, cool surfaces.
 
- **Primary (`#00446f`) & Primary Container (`#005c94`):** Representing the core stability of the firm.
- **Secondary (`#006e27`):** Reserved strictly for high-conversion CTAs and success states, symbolizing growth.
- **Surface Hierarchy:** We utilize a light-blue tinted neutral scale (`#f7fafd` to `#e0e3e6`) to build depth.
 
### The "No-Line" Rule
**Explicit Instruction:** 1px solid borders are prohibited for sectioning. We do not use "boxes" to contain ideas. Boundaries must be defined solely through background color shifts. For example, a `surface-container-low` section should sit directly against a `surface` background to define its edge.
 
### Surface Hierarchy & Nesting
Treat the UI as a series of nested layers.
* **Base:** `surface` (#f7fafd)
* **Secondary Sections:** `surface-container-low` (#f1f4f7)
* **Interactive Cards:** `surface-container-lowest` (#ffffff) sitting on a darker surface creates a natural, soft lift.
 
### The "Glass & Gradient" Rule
To add "soul" to the corporate structure:
* **Glassmorphism:** Use semi-transparent `surface` colors with a `backdrop-blur: 20px` for the sticky navbar and floating WhatsApp button.
* **Signature Textures:** Main Hero backgrounds should use a subtle linear gradient from `primary` (#00446f) to `primary-container` (#005c94) at a 135-degree angle to avoid a "flat" digital feel.
 
---
 
## 3. Typography
We use a high-contrast scale to establish a clear information hierarchy.
 
- **Display & Headline (Be Vietnam Pro):** Our "Voice." Bold, geometric, and unapologetically large. Headlines should feel architectural—providing the structural anchors for the page.
- **Body & Labels (Inter):** Our "Engine." Clean, highly legible, and neutral.
- **The Editorial Shift:** Use `display-lg` (3.5rem) for hero statements to command attention. Use `label-md` with 0.05em letter-spacing for "overlines" (small text above headlines) to create a sophisticated, curated look.
 
---
 
## 4. Elevation & Depth
Depth is achieved through **Tonal Layering** rather than traditional drop shadows.
 
### The Layering Principle
Stacking surface tokens creates a sophisticated "paper-on-paper" look.
* Place a `surface-container-lowest` (#ffffff) card on a `surface-container-low` (#f1f4f7) section. The delta in hex value is enough to signify elevation without visual clutter.
 
### Ambient Shadows
Shadows are only permitted for "Floating" elements (e.g., the WhatsApp CTA or active Modals).
* **Style:** Extra-diffused. `box-shadow: 0 20px 40px rgba(0, 14, 63, 0.06);`
* **Note:** Use a tiny percentage of the Deep Navy (`on-surface`) for the shadow color to ensure it looks like a natural occlusion of light, never a "grey" smudge.
 
### The "Ghost Border" Fallback
If a container requires a boundary for accessibility, use the `outline-variant` token at **15% opacity**. It should be felt, not seen.
 
---
 
## 5. Components
 
### Buttons
* **Primary (Secondary Token `#006e27`):** Solid fill, `on-secondary` text. High-contrast for the main CTA.
* **Secondary (Primary Token `#00446f`):** Solid fill for secondary firm actions.
* **Ghost/Tertiary:** No fill, `primary` text. Use for less critical navigation.
* **Corner Radius:** Use `subtle` (1) for a professional, slightly softened geometric feel.
 
### Input Fields
* **Background:** `surface-container-highest` (#e0e3e6).
* **Border:** None, except for a 2px `primary` bottom-border on focus.
* **Label:** `label-md` placed strictly above the field, never as a placeholder.
 
### Cards & Lists
* **Rule:** Forbid divider lines.
* **Execution:** Separate list items using `spacing-4` (1.4rem) of vertical whitespace. In cards, use a change in typography weight or a subtle background shift (`surface-container-low`) for the footer area of the card.
 
### Featured Component: "The Trust Bar"
A horizontally scrolling or static row of client logos/certifications. Use a `backdrop-blur` background and "Ghost Borders" to make this feel like a floating piece of glass over the content.
 
---
 
## 6. Do's and Don'ts
 
### Do
* **DO** use the Blue Logo on `surface` backgrounds and the White Logo on `primary` or `tertiary` (Navy) backgrounds.
* **DO** embrace extreme asymmetry. Align a headline to the left and the body copy to the far right of the grid to create an editorial feel.
* **DO** use `spacing-16` or `spacing-20` between major sections to let the design breathe.
 
### Don't
* **DON'T** use 100% black. Use `on-background` (#181c1e) for text to maintain a premium, softer contrast.
* **DON'T** distort the logo. Maintain the aspect ratio religiously.
* **DON'T** use standard "Box Shadows" on cards. Rely on tonal shifts between `surface-container` levels.
* **DON'T** use the secondary green for anything other than "Growth" related CTAs (e.g., Contact, Start Quote).
 
---
*This system is designed to convey the precision of an accountant and the vision of a partner. Ensure every pixel serves a purpose.*