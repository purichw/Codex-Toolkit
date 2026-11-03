import { StatusBadge, type BadgeTone, type StatusBadgeProps } from "../../shared/ui";

export type MembershipStatus = "active" | "under-review" | "expired";

const presentation = {
  active: { label: "สมาชิกปัจจุบัน", tone: "positive" },
  "under-review": { label: "กำลังตรวจสอบเอกสาร", tone: "caution" },
  expired: { label: "สมาชิกหมดอายุ", tone: "negative" },
} satisfies Record<MembershipStatus, { label: string; tone: BadgeTone }>;

export type MembershipStatusBadgeProps = Omit<StatusBadgeProps, "children" | "tone"> & {
  status: MembershipStatus;
};

/**
 * Membership owns its vocabulary and future changes independently of bookings.
 * Keep this feature wrapper explicit even when another feature uses the same tone.
 * Validate unknown service data before it reaches this typed component.
 */
export function MembershipStatusBadge({ status, ...nativeProps }: MembershipStatusBadgeProps) {
  const { label, tone } = presentation[status];
  return <StatusBadge {...nativeProps} tone={tone}>{label}</StatusBadge>;
}
