import * as React from "react";
import {getResourceUrl} from "api/utils";


export function ViewContainer({ children }: { children: React.ReactElement | React.ReactElement[] }) {
    return <div style={{
        position: 'absolute',
        top: '0px', left: '0px',
        width: '100%', height: '100%',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center'
    }}>
        <div style={{
            position: 'absolute',
            top: '-20px', left: '-20px',
            width: 'calc(100% + 40px)', height: 'calc(100% + 40px)',
            filter: 'blur(8px)',
            backgroundPosition: 'center',
            backgroundSize: 'cover',
            zIndex: '-1',
            backgroundImage: `url(${getResourceUrl('base:textures.ui.background.background.png')})`
        }}>
        </div>

        <div style={{
            display: 'flex',
            flexDirection: 'column',
            backgroundColor: 'white',
            padding: '24px',
            borderRadius: '10px',
            gap: '16px',
            width: '500px',
            boxShadow: '0px 0px 10px black',
            maxHeight: 'calc(100vh - 100px)',
            overflow: 'auto'
        }}>
            {children}
        </div>
    </div>
}