import type { ComponentPropsWithoutRef } from "react";

/** Visual vocabulary only. Business statuses belong to their feature. */
export type BadgeTone = "neutral" | "positive" | "caution" | "negative";

export type StatusBadgeProps = Omit<
  ComponentPropsWithoutRef<"span">,
  "children" | "dangerouslySetInnerHTML"
> & {
  children: string;
  tone?: BadgeTone;
};

/**
 * Render readable text with a visual tone. Color is never the only status cue.
 * Native span attributes are supported; this noninteractive component exposes
 * no ref contract. Do not add a live region to every badge in a data table.
 * Import the example's components.css once at the application composition root.
 */
export function StatusBadge({
  children,
  tone = "neutral",
  className,
  ...nativeProps
}: StatusBadgeProps) {
  return (
    <span
      {...nativeProps}
      className={["sc-status-badge", className].filter(Boolean).join(" ")}
      data-tone={tone}
    >
      {children}
    </span>
  );
}
