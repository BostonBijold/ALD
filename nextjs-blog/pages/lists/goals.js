import Link from "next/link";
import Layout from "../../components/layout";

export default function goals() {
    return (
        <Layout>
            <h1>My Goals</h1>
            <h2>
                <Link href="/">Back to home</Link>
            </h2>
        </Layout>
    );
}