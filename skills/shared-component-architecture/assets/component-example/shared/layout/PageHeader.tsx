import type { ComponentPropsWithoutRef, ReactNode } from "react";

export type PageHeaderProps = Omit<
  ComponentPropsWithoutRef<"header">,
  "children" | "title" | "dangerouslySetInnerHTML"
> & {
  title: string;
  headingId: string;
  description?: string;
  actions?: ReactNode;
};

/**
 * This is a page-level header, so it owns an h1. A section header should have a
 * separate explicit contract if needed. Consumers own action behavior, routing,
 * permission decisions, and spacing between this header and the next section.
 * The actions slot is ordinary content, not an ARIA toolbar or menu widget.
 */
export function PageHeader({
  title,
  headingId,
  description,
  actions,
  className,
  ...nativeProps
}: PageHeaderProps) {
  return (
    <header
      {...nativeProps}
      className={["sc-page-header", className].filter(Boolean).join(" ")}
    >
      <div className="sc-page-header__copy">
        <h1 id={headingId}>{title}</h1>
        {description ? <p>{description}</p> : null}
      </div>
      {actions != null ? <div className="sc-page-header__actions">{actions}</div> : null}
    </header>
  );
}
