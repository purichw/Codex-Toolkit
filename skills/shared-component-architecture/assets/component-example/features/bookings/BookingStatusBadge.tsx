import { StatusBadge, type BadgeTone, type StatusBadgeProps } from "../../shared/ui";

export type BookingStatus = "confirmed" | "awaiting-confirmation" | "cancelled";

const presentation = {
  confirmed: { label: "ยืนยันแล้ว", tone: "positive" },
  "awaiting-confirmation": { label: "รอการยืนยัน", tone: "caution" },
  cancelled: { label: "ยกเลิก", tone: "neutral" },
} satisfies Record<BookingStatus, { label: string; tone: BadgeTone }>;

export type BookingStatusBadgeProps = Omit<StatusBadgeProps, "children" | "tone"> & {
  status: BookingStatus;
};

/**
 * The booking feature owns labels and their meaning. Adding a booking status
 * changes this exhaustive mapping without adding business knowledge to shared UI.
 * Values here are already domain-validated. Decode unknown API strings in the
 * booking data adapter; do not cast an unchecked backend string to BookingStatus.
 * In a localized application, resolve labels through the feature's translation
 * layer while keeping the shared badge independent of locale/provider choice.
 */
export function BookingStatusBadge({ status, ...nativeProps }: BookingStatusBadgeProps) {
  const { label, tone } = presentation[status];
  return <StatusBadge {...nativeProps} tone={tone}>{label}</StatusBadge>;
}
