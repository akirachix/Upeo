// Sidebar imports
import {
  UilEstate,
  UilClipboardAlt,
  UilUsersAlt,
  UilPackage,
  UilChart,
} from "@iconscout/react-unicons";

// Analytics Cards imports
import { UilUsdSquare, UilMoneyWithdrawal } from "@iconscout/react-unicons";

// Recent Card Imports

// Sidebar Data
export const SidebarData = [
  {
    icon: UilEstate,
    heading: "Dashboard",
  },
  {
    icon: UilClipboardAlt,
    heading: "Questions",
  },
  {
    icon: UilUsersAlt,
    heading: "Students",
  },
  {
    icon: UilPackage,
    heading: 'Answers'
  },
  {
    icon: UilChart,
    heading: 'Grades'
  },
];

// Analytics Cards Data
export const cardsData = [
  {
    title: "Students",
    color: {
      backGround: "linear-gradient(180deg, #bb67ff 0%, #84d9f3 100%)",
      boxShadow: "0px 10px 20px 0px #84d9f3",
    },
    barValue: 70,
    png: UilUsdSquare,
    series: [
      {
        name: "Students",
        data: [29, 70, 3, 13, 45, 56, 50],
      },
    ],
  },
  {
    title: "Teenage Pregnancies",
    color: {
      backGround: "linear-gradient(180deg, #bb67ff 0%, #84d9f3 100%)",
      boxShadow: "0px 10px 20px 0px #84d9f3",
    },
    barValue: 80,
    png: UilMoneyWithdrawal,
    series: [
      {
        name: "Teenage Pregnancies",
        data: [10000, 20000, 222000,650000],
      },
    ],
  },

];

// Recent Update Card Data
export const UpdatesData = [

];
