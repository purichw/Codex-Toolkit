/**
 * Compile-only checks for public contracts. Run tsc --noEmit with strict: true
 * and jsx: react-jsx in a React + TypeScript project. These are NOT runtime,
 * accessibility, or visual tests. Preserve @ts-expect-error checks: tsc reports
 * an error if a forbidden example accidentally becomes accepted.
 */
import { StatusBadge, type BadgeTone } from "./shared/ui";
import { PageHeader } from "./shared/layout";
import { BookingStatusBadge } from "./features/bookings";
import { MembershipStatusBadge } from "./features/membership";
import { BookingsExamplePage, MembershipExamplePage } from "./consumers";

<StatusBadge tone="positive" lang="th">พร้อมใช้งาน</StatusBadge>;
<PageHeader title="รายการ" headingId="test-title" actions={<a href="#items">ดูรายการ</a>} />;
<BookingStatusBadge status="confirmed" title="นัดหมายได้รับการยืนยันแล้ว" />;
<MembershipStatusBadge status="active" />;
<BookingsExamplePage />;
<MembershipExamplePage />;

// @ts-expect-error — palette names are not semantic tones in this public API.
const unsupportedTone: BadgeTone = "purple";
void unsupportedTone;
// @ts-expect-error — membership vocabulary cannot leak into booking consumers.
<BookingStatusBadge status="active" />;
// @ts-expect-error — booking vocabulary cannot leak into membership consumers.
<MembershipStatusBadge status="confirmed" />;
// @ts-expect-error — feature wrappers own their semantic presentation.
<BookingStatusBadge status="confirmed" tone="negative" />;
// @ts-expect-error — visible readable status text is required by the primitive.
<StatusBadge tone="positive" />;

// @ts-expect-error - the badge owns its escaped text, not raw HTML.
<StatusBadge dangerouslySetInnerHTML={{ __html: "<b>Unsafe override</b>" }}>Ready</StatusBadge>;
// @ts-expect-error - the header owns its heading and slots.
<PageHeader title="Items" headingId="items-title" dangerouslySetInnerHTML={{ __html: "Override" }} />;
// @ts-expect-error - domain wrappers retain the primitive's content boundary.
<MembershipStatusBadge status="active" dangerouslySetInnerHTML={{ __html: "Override" }} />;
