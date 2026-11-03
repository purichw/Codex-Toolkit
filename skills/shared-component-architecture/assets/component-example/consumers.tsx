/**
 * Two independent route compositions for React + TypeScript, not a complete app.
 * Render ONE of these pages under the application's normal layout, and import
 * components.css once there. Replace fixture data with a validated feature model.
 * Each page owns its actions and local composition; shared components never
 * import a feature, router, backend SDK, or global business store.
 * Use existing project primitives for links/buttons when integrating this sample.
 */
import { PageHeader } from "./shared/layout";
import { BookingStatusBadge } from "./features/bookings";
import { MembershipStatusBadge } from "./features/membership";

export function BookingsExamplePage() {
  return (
    <main className="sc-example-page" aria-labelledby="bookings-title">
      <PageHeader
        headingId="bookings-title"
        title="การนัดหมาย"
        description="ตรวจวัน เวลา และสถานะของนัดหมายในรายการ"
        actions={<a href="#bookings-list">ไปยังรายการนัดหมาย</a>}
      />
      <section id="bookings-list" aria-label="รายการนัดหมายตัวอย่าง">
        <h2>ปรึกษาโปรแกรมฝึกส่วนตัว</h2>
        <p>ณัฐณิชา ธรรมรักษ์วัฒนกุล · 3 พฤศจิกายน 2026 เวลา 09:30 น.</p>
        <BookingStatusBadge status="awaiting-confirmation" />
      </section>
    </main>
  );
}

export function MembershipExamplePage() {
  return (
    <main className="sc-example-page" aria-labelledby="membership-title">
      <PageHeader
        headingId="membership-title"
        title="สถานะสมาชิก"
        description="ตรวจรายละเอียดและสถานะคำขอสมัครสมาชิก"
        actions={<a href="#membership-details">ดูรายละเอียดคำขอ</a>}
      />
      <section id="membership-details" aria-label="คำขอสมัครสมาชิกตัวอย่าง">
        <h2>คำขอสมัครสมาชิกเลขที่ DEMO-018</h2>
        <p>ตัวอย่างนี้แสดงข้อมูลสมมติ โดยการอนุมัติเป็นหน้าที่ของระบบสมาชิก</p>
        <MembershipStatusBadge status="under-review" />
      </section>
    </main>
  );
}
