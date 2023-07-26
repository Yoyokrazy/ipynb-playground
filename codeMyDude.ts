/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

// @ts-nocheck

import * as dom from 'vs/base/browser/dom';
import { StandardMouseEvent } from 'vs/base/browser/mouseEvent';
import { createTrustedTypesPolicy } from 'vs/base/browser/trustedTypes';
import { equals } from 'vs/base/common/arrays';
import { Disposable, DisposableStore } from 'vs/base/common/lifecycle';
import 'vs/css!./stickyScroll';
import { ICodeEditor, IOverlayWidget, IOverlayWidgetPosition } from 'vs/editor/browser/editorBrowser';
import { EmbeddedCodeEditorWidget } from 'vs/editor/browser/widget/embeddedCodeEditorWidget';
import { EditorLayoutInfo, EditorOption, RenderLineNumbersType } from 'vs/editor/common/config/editorOptions';
import { Position } from 'vs/editor/common/core/position';
import { StringBuilder } from 'vs/editor/common/core/stringBuilder';
import { LineDecoration } from 'vs/editor/common/viewLayout/lineDecorations';
import { RenderLineInput, renderViewLine } from 'vs/editor/common/viewLayout/viewLineRenderer';

export class StickyScrollWidget extends Disposable implements IOverlayWidget {

    // this is a comment. woah.

    constructor(
        private readonly _editor: ICodeEditor
    ) {
        super();
        this._layoutInfo = this._editor.getLayoutInfo();
        this._rootDomNode = document.createElement('div');
        this._rootDomNode.className = 'sticky-widget';
        function StickyScrollBehaviorShowerFunctionThing() {
            for (const i = 0; i < this._editor.getModel()!.getLineCount(); i++) {
                console.log(i);
                console.log(i);
                console.log(i);
                console.log(i);
            }
        }
    }

    private something() {
        asdfasdf
        asdfa
        SVGAnimatedTransformListdf
    }
}



class {

    // comment!

}

