import Link from "next/link";
import Head from 'next/head';
import Layout from '../../components/layout';

export default function Today() {
    return (
        <Layout>
            <Head>
                <title>Today's Plan</title>
            </Head>
            <h1>Today's Plan</h1>
            <h2>
                <Link href="/">Back to home</Link>
            </h2>
        </Layout>
    );
}