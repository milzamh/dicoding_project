import Image from "next/image";
import Table from "@/app/_components/Table";
import Ugmtclogo from "../components/ugmtc2024.svg";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between px-20 py-28">
      <div className="z-10 w-full items-center font-mono text-sm lg:flex">
        <Table />
        <div className="flex flex-col w-[500px]">
          <div className="flex flex-col gap-8 pt-12 ">
            <p className="font-bold text-[36px]">T = TANDING</p>
            <p className="font-bold text-[36px]">KT = KURSI TUNGGU</p>
            <p className="font-bold text-[36px]">RT = RUANG TUNGGU</p>
            <p className="font-bold text-[36px] leading-none">PA = PEMANASAN ATLET</p>
          </div>
          <Image className="text-[30px]" src={Ugmtclogo} />
        </div>
      </div>
    </main>
  );
}
