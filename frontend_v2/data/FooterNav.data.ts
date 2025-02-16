interface Child {
  name: string;
  url: string;
}

export interface FooterNavData {
  id: number,
  title: string;
  items: Child[];
}

export const FOOTER_NAV_PRODUCT_DATA: FooterNavData[] = [
  {
    id: 1,
    title: 'product',
    items: [
      {
        name: 'about',
        url: '/about',
      },
      {
        name: 'contact',
        url: '/contact',
      },
      {
        name: 'terms',
        url: '/terms',
      },
    ]
  },
  {
    id: 2,
    title: 'possibilities',
    items: [
      {
        name: 'how',
        url: '/how',
      },
      {
        name: 'better',
        url: '/login',
      },
    ]
  }
]