"use client";
import { useState } from "react";
import React from "react";
import Image from "next/image";

const Table = () => {
  const [numbersA, setNumbersA] = useState([1, 2, 3, 4, 5, 6]);
  const [numbersB, setNumbersB] = useState([1, 2, 3, 4, 5, 6]);
  const [numbersC, setNumbersC] = useState([1, 2, 3, 4, 5, 6]);
  const [numbersD, setNumbersD] = useState([1, 2, 3, 4, 5, 6]);
  const [numbersE, setNumbersE] = useState([1, 2, 3, 4, 5, 6]);

  const handleClick = (setNumbers) => {
    setNumbers((prevNumbers) => prevNumbers.map((num) => (num % 999) + 1));
  };

  return (
    <div className="flex p-0 gap-8">
      <div className="flex flex-col gap-3">
        <div className="flex gap-6 mr-12">
          <div className="w-[100px] h-[100px] bg-white flex items-center justify-center">
            <p className="font-bold text-[40px] text-white">T</p>
          </div>
          <div className="w-[100px] h-[100px] bg-gray-400 flex items-center justify-center">
            <p className="font-bold text-[40px] text-white">T</p>
          </div>
          <div className="w-[100px] h-[100px] bg-gray-400 flex items-center justify-center">
            <p className="font-bold text-[40px] text-white">KT</p>
          </div>
          <div className="w-[100px] h-[100px] bg-gray-400 flex items-center justify-center">
            <p className="font-bold text-[40px] text-white">RT</p>
          </div>
          <div className="w-[100px] h-[100px] bg-gray-400 flex items-center justify-center">
            <p className="font-bold text-[40px] text-white">RT</p>
          </div>
          <div className="w-[100px] h-[100px] bg-gray-400 flex items-center justify-center">
            <p className="font-bold text-[40px] text-white">RT</p>
          </div>
          <div className="w-[100px] h-[100px] bg-gray-400 flex items-center justify-center">
            <p className="font-bold text-[40px] text-white">PA</p>
          </div>
        </div>
        <div className="flex gap-6">
          <button onClick={() => handleClick(setNumbersA)}>
            <div className="w-[100px] h-[100px] bg-orange-400 flex items-center justify-center">
              <p className="font-bold text-[40px] text-white">A</p>
            </div>
          </button>
          {numbersA.map((num, index) => (
            <div
              key={index}
              className={`w-[100px] h-[100px] bg-[${getColor(
                index
              )}] flex items-center justify-center`}
            >
              <p className="font-bold text-[40px] text-black">{num}</p>
            </div>
          ))}
        </div>
        <div className="flex gap-6">
          <button onClick={() => handleClick(setNumbersB)}>
            <div className="w-[100px] h-[100px] bg-orange-400 flex items-center justify-center">
              <p className="font-bold text-[40px] text-white">B</p>
            </div>
          </button>
          {numbersB.map((num, index) => (
            <div
              key={index}
              className={`w-[100px] h-[100px] bg-[${getColor(
                index
              )}] flex items-center justify-center`}
            >
              <p className="font-bold text-[40px] text-black">{num}</p>
            </div>
          ))}
        </div>
        <div className="flex gap-6">
          <button onClick={() => handleClick(setNumbersC)}>
            <div className="w-[100px] h-[100px] bg-orange-400 flex items-center justify-center">
              <p className="font-bold text-[40px] text-white">C</p>
            </div>
          </button>
          {numbersC.map((num, index) => (
            <div
              key={index}
              className={`w-[100px] h-[100px] bg-[${getColor(
                index
              )}] flex items-center justify-center`}
            >
              <p className="font-bold text-[40px] text-black">{num}</p>
            </div>
          ))}
        </div>
        <div className="flex gap-6">
          <button onClick={() => handleClick(setNumbersD)}>
            <div className="w-[100px] h-[100px] bg-orange-400 flex items-center justify-center">
              <p className="font-bold text-[40px] text-white">D</p>
            </div>
          </button>
          {numbersD.map((num, index) => (
            <div
              key={index}
              className={`w-[100px] h-[100px] bg-[${getColor(
                index
              )}] flex items-center justify-center`}
            >
              <p className="font-bold text-[40px] text-black">{num}</p>
            </div>
          ))}
        </div>
        <div className="flex gap-6">
          <button onClick={() => handleClick(setNumbersE)}>
            <div className="w-[100px] h-[100px] bg-orange-400 flex items-center justify-center">
              <p className="font-bold text-[40px] text-white">E</p>
            </div>
          </button>
          {numbersE.map((num, index) => (
            <div
              key={index}
              className={`w-[100px] h-[100px] bg-[${getColor(
                index
              )}] flex items-center justify-center`}
            >
              <p className="font-bold text-[40px] text-black">{num}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
const getColor = (index) => {
  const colors = [
    "#7575E2",
    "#5FB59C",
    "#97DFAF",
    "#97DFAF",
    "#97DFAF",
    "#DEEFB8",
  ];
  return colors[index];
};

export default Table;
